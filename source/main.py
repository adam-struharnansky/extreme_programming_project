import logging
import os
import pygame
import sys

# this line makes the directory one level above the root directory from which the relative imports are made
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))

from auxiliary import WHITE
from auxiliary import Direction, GameState, KeyStates, MapType, MapSize
from auxiliary import setup_logging
from front_end import Menu
from game.maps import Map

# constants
SIZE = WIDTH, HEIGHT = 700, 770
MENU_HEIGHT = 50
MENU_SCREEN_SIZE = (WIDTH, MENU_HEIGHT)
MAP_SCREEN_SIZE = (WIDTH, HEIGHT - MENU_HEIGHT)
BACKGROUND_COLOR = WHITE

# variables
next_map_type = MapType.RANDOM
next_map_size = MapSize.SMALL
saving = False
state_of_game = GameState.MENU
key_states = {Direction.RIGHT: KeyStates.UNPRESSED, Direction.LEFT: KeyStates.UNPRESSED,
              Direction.DOWN: KeyStates.UNPRESSED, Direction.UP: KeyStates.UNPRESSED}

# calling necessary components from pygame
setup_logging(level=logging.DEBUG)
pygame.init()
screen = pygame.display.set_mode(SIZE)

menu_screen = pygame.Surface(MENU_SCREEN_SIZE)
map_screen = pygame.Surface(MAP_SCREEN_SIZE)

pygame.display.set_caption('Pygame Basic Window')

menu = Menu(screen)
game_map = Map(map_screen, menu_screen, debug=True)

logging.info('Start Menu')


def handle_key_press(direction, pressed):
    if pressed:
        if key_states[direction] == KeyStates.UNPRESSED:
            key_states[direction] = KeyStates.PRESSED
    else:
        key_states[direction] = KeyStates.UNPRESSED


def handle_keys():
    keys = pygame.key.get_pressed()
    screen.blit(menu_screen, (0, 0))
    screen.blit(map_screen, (0, MENU_HEIGHT))

    handle_key_press(Direction.UP, keys[pygame.K_UP] or keys[pygame.K_w])
    handle_key_press(Direction.DOWN, keys[pygame.K_DOWN] or keys[pygame.K_s])
    handle_key_press(Direction.LEFT, keys[pygame.K_LEFT] or keys[pygame.K_a])
    handle_key_press(Direction.RIGHT, keys[pygame.K_RIGHT] or keys[pygame.K_d])

    for i in key_states.keys():
        if key_states[i] == KeyStates.PRESSED:
            game_map.move(i)
            key_states[i] = KeyStates.PROCESSED
            logging.debug(f'Processing direction: {i}')


def handle_button(menu_buttons):
    for button in menu_buttons:
        response = button.handle_event(event)
        if response is not None:
            return response
    return None


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

        next_map_size = menu.map_size()
        next_map_type = menu.map_type()

        response = handle_button(menu.base_menu_buttons)

        if response == "New Game":
            state_of_game = GameState.LOADING_NEW_GAME
        elif response == "Load Game":
            state_of_game = GameState.LOADING_EXISTING_GAME
        elif response == "Exit Game":
            break

    if state_of_game == GameState.LOADING_NEW_GAME:
        try:
            game_map.generate_map(next_map_size.value[0], next_map_size.value[1], next_map_type)
            game_map.draw()
            state_of_game = GameState.PLAYING_GAME
        except ValueError:
            logging.warning(f'Wrong arguments for generating a map')

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
