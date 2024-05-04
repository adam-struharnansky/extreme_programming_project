import sys
import os

# this line makes the directory one level above the root directory from which the relative imports are made
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))

import pygame
import logging

from auxiliary import WHITE
from auxiliary import GameState, Key
from auxiliary import setup_logging
from front_end import Menu
from game.maps import Map

# constants
SIZE = WIDTH, HEIGHT = 700, 770
MENU_HEIGHT = 50
BACKGROUND_COLOR = WHITE
# todo: Instead of strings use enums for types of the maps
MAP_PARAMS = {'biome_type': 'random', 'sizes': {'row_number': 50, 'column_number': 50}}

setup_logging(level=logging.DEBUG)
pygame.init()
screen = pygame.display.set_mode(SIZE)

menu_screen_size = (WIDTH, MENU_HEIGHT)
map_screen_size = (WIDTH, HEIGHT - MENU_HEIGHT)

menu_screen = pygame.Surface(menu_screen_size)
map_screen = pygame.Surface(map_screen_size)

pygame.display.set_caption('Pygame Basic Window')

state_of_game = GameState.MENU
key_states = {}  # left, right, up, down
saving = False

menu = Menu(screen)
game_map = Map(map_screen, menu_screen, debug=True)

logging.info('Start Menu')


def handle_keys():
    keys = pygame.key.get_pressed()
    screen.blit(menu_screen, (0, 0))
    screen.blit(map_screen, (0, MENU_HEIGHT))
    # todo: Change these magic constants (key_states = 0, 1, 2) to some understandable enum

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if key_states[pygame.K_RIGHT] < 1:
            key_states[pygame.K_RIGHT] = 1
    else:
        key_states[pygame.K_RIGHT] = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if key_states[pygame.K_LEFT] < 1:
            key_states[pygame.K_LEFT] = 1
    else:
        key_states[pygame.K_LEFT] = 0

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if key_states[pygame.K_DOWN] < 1:
            key_states[pygame.K_DOWN] = 1
    else:
        key_states[pygame.K_DOWN] = 0

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if key_states[pygame.K_UP] < 1:
            key_states[pygame.K_UP] = 1
    else:
        key_states[pygame.K_UP] = 0

    for i in key_states.keys():
        if key_states[i] == 1:
            key_states[i] = 2
            game_map.move(i)
            match i:
                case Key.RIGHT.value:
                    logging.debug("right")
                case Key.LEFT.value:
                    logging.debug("left")
                case Key.DOWN.value:
                    logging.debug("down")
                case Key.UP.value:
                    logging.debug("up")
                case _:
                    logging.warning("Achievement unlocked: How did we get here?")


def handle_button(menu_button):
    for button in menu_button:
        temp_response = button.handle_event(event)
        if temp_response is not None:
            response = temp_response
            break
    else:
        response = None

    return response


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    if state_of_game == GameState.MENU:
        menu.handle_event(event)  # todo: Why doesn't this need to be initialized?
        menu.draw_base_menu()
        menu.draw_size_options()

        for opt_button in menu.menu_buttons:
            if opt_button.is_checked:
                MAP_PARAMS[opt_button.option['label']] = opt_button.option['value']


        response = handle_button(menu.base_menu_buttons)

        if response == "New Game":
            state_of_game = GameState.LOADING_NEW_GAME
        elif response == "Load Game":
            state_of_game = GameState.LOADING_EXISTING_GAME
        elif response == "Exit Game":
            break

    if state_of_game == GameState.LOADING_NEW_GAME:
        if MAP_PARAMS['biome_type'] == 'random':
            game_map.generate_random_map(row_count=MAP_PARAMS["sizes"]['row_number'],
                                         column_count=MAP_PARAMS['sizes']['column_number'])
        elif MAP_PARAMS['biome_type'] == 'Biomes map':
            game_map.generate_biomes_map(row_count=MAP_PARAMS["sizes"]['row_number'],
                                         column_count=MAP_PARAMS['sizes']['column_number'], biome_count=5)
        else:
            game_map.generate_biomes_map(row_count=MAP_PARAMS["sizes"]['row_number'],
                                         column_count=MAP_PARAMS['sizes']['column_number'], biome_count=20)
        game_map.draw()
        state_of_game = GameState.PLAYING_GAME

    if state_of_game == GameState.LOADING_EXISTING_GAME:
        game_map.load_map()
        game_map.draw()
        state_of_game = GameState.PLAYING_GAME

    if state_of_game == GameState.PLAYING_GAME:
        handle_keys()
        game_map.draw()
        menu.draw_in_game_buttons()

        response = handle_button(menu.in_game_buttons)
        
        # todo: Instead of using strings for response, create some enums for this
        if response == "Save Game" and not saving:
            logging.info("Map saved")
            saving = True
            game_map.save_map()
        elif response == "Exit to Menu":
            state_of_game = GameState.MENU
        elif response is None:
            saving = False


        response = handle_button(menu.lost_game_buttons)

        if response == "Main menu":
            state_of_game = GameState.MENU

    pygame.display.flip()
