import logging
import os
import pygame
import sys

# this line makes the directory one level above the root directory from which the relative imports are made
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))

from auxiliary import Direction, GameState, KeyStates, MapType, MapSize
from auxiliary import setup_logging
from front_end import Menu
from game.maps import Map

# constants
SIZE = WIDTH, HEIGHT = 700, 770
MENU_HEIGHT = 50
MENU_SCREEN_SIZE = (WIDTH, MENU_HEIGHT)
MAP_SCREEN_SIZE = (WIDTH, HEIGHT - MENU_HEIGHT)
SAVE_COOLDOWN = 1000  # milliseconds

# variables
next_map_type = MapType.RANDOM
next_map_size = MapSize.SMALL
saving = False
game_state = GameState.MENU_INITIALIZATION
previous_game_state = GameState.EXIT
key_states = {Direction.RIGHT: KeyStates.UNPRESSED, Direction.LEFT: KeyStates.UNPRESSED,
              Direction.DOWN: KeyStates.UNPRESSED, Direction.UP: KeyStates.UNPRESSED}
last_saved = 0

# calling necessary components from pygame
setup_logging(level=logging.DEBUG)
pygame.init()
screen = pygame.display.set_mode(SIZE)

menu_screen = pygame.Surface(MENU_SCREEN_SIZE)
map_screen = pygame.Surface(MAP_SCREEN_SIZE)

pygame.display.set_caption('Pygame Basic Window')

menu = Menu(screen)
game_map = Map(map_screen, menu_screen, debug=True)

logging.info('Start of the Game')


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


while True:
    if previous_game_state != game_state:
        logging.info(f'State of the Game: {game_state}')
        previous_game_state = game_state
    event = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    match game_state.value:
        case GameState.MENU_INITIALIZATION.value:
            menu.draw_base_menu()
            game_state = GameState.MENU
        case GameState.MENU.value:
            menu.recheck_map_checkboxes(event)
            next_map_size = menu.map_size()
            next_map_type = menu.map_type()
            game_state = menu.base_menu_response(event)
        case GameState.LOADING_NEW_GAME.value:
            try:
                game_map.generate_map(next_map_size.value, next_map_type)
                game_map.draw()
                game_state = GameState.PLAYING_GAME
            except ValueError:
                logging.error(f'Wrong arguments for generating a map')
                game_state = GameState.MENU_INITIALIZATION
        case GameState.LOADING_EXISTING_GAME.value:
            # todo: Add loading any file in the directory (make some way how to pick them)
            try:
                game_map.load_map()
                game_state = GameState.PLAYING_GAME
            except FileNotFoundError:
                logging.error('Error: Pickle file for map not found')
                game_state = GameState.MENU_INITIALIZATION
            except ValueError as valueError:
                logging.error(valueError)
                game_state = GameState.MENU_INITIALIZATION
        case GameState.PLAYING_GAME.value:
            handle_keys()
            game_map.draw()
            menu.draw_in_game_buttons()  # todo: Does this need to be redrawn every time?
            game_state = GameState.LOST_GAME if game_map.is_game_lost() else menu.in_game_response(event)
        case GameState.SAVING_GAME.value:
            if pygame.time.get_ticks() - last_saved > SAVE_COOLDOWN:
                game_map.save_map()
                logging.info('Map saved')
                last_saved = pygame.time.get_ticks()
                game_state = GameState.PLAYING_GAME
        case GameState.LOST_GAME.value:
            # todo: Add stuff for Game Over: show button for returning to the main menu, maybe some stats..
            game_state = menu.lost_game_response(event)
        case GameState.EXIT.value:
            break
    pygame.display.flip()
