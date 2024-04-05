import pygame
import sys

from colors import WHITE
from enums import GameState, Key
from map import Map
from menu import Menu

DEBUG_ALL = False
DEBUG_KEY = True
DEBUG_MOVE = True
SIZE = WIDTH, HEIGHT = 700, 770
MENU_HEIGHT = 50
BACKGROUND_COLOR = WHITE

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
game_map = Map(map_screen, menu_screen, debug=DEBUG_ALL or DEBUG_MOVE)


def handle_keys():
    keys = pygame.key.get_pressed()
    screen.blit(menu_screen, (0, 0))
    screen.blit(map_screen, (0, MENU_HEIGHT))
    # todo: Zmenit tieto magicke konstanty na nejaky enum

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
            if DEBUG_KEY:
                match i:
                    case Key.RIGHT.value:
                        print("right")
                    case Key.LEFT.value:
                        print("left")
                    case Key.DOWN.value:
                        print("down")
                    case Key.UP.value:
                        print("up")
                    case _:
                        print("Achievement unlocked: How did we get here?")
                # ----------------------------------------------------------------------------------------------
                # docasne, iba pre testovanie, ci funguje pridavanie equipmentu
                # todo: Presunut toto do do map.py, kde to bude spustene ked hrac pride na policko s loot-om
                import item_generator
                import random
                from enums import ItemLevel
                tmp_rnd = random.random()
                if tmp_rnd <= 0.25:
                    game_map._dat.player.add_item_equipment(item_generator.generate_random_armor(ItemLevel.BRONZE))
                elif 0.25 < tmp_rnd <= 0.5:
                    game_map._dat.player.add_item_equipment(item_generator.generate_random_armor(ItemLevel.SILVER))
                elif 0.5 < tmp_rnd <= 0.75:
                    game_map._dat.player.add_item_equipment(item_generator.generate_random_armor(ItemLevel.GOLD))
                else:
                    game_map._dat.player.add_item_equipment(item_generator.generate_random_armor(ItemLevel.LEGENDARY))
                # -----------------------------------------------------------------------------------------------


while True:
    for event in pygame.event.get():
        if DEBUG_ALL:
            if event.type != pygame.MOUSEMOTION:
                print("Event: " + str(event))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    if state_of_game == GameState.MENU:
        menu.draw_base_menu()

        for button in menu.base_menu_buttons:
            temp_response = button.handle_event(event)
            if temp_response is not None:
                response = temp_response
                break
        else:
            response = None

        if response == "New Game":
            state_of_game = GameState.LOADING_NEW_GAME
        elif response == "Load Game":
            state_of_game = GameState.LOADING_EXISTING_GAME
        elif response == "Exit Game":
            break

    if state_of_game == GameState.LOADING_NEW_GAME:
        game_map.generate_map()
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

        for button in menu.in_game_buttons:
            temp_response = button.handle_event(event)
            if temp_response is not None:
                response = temp_response
                break
        else:
            response = None

        if response == "Save Game" and not saving:
            if DEBUG_ALL:
                print("Map saved")
            saving = True
            game_map.save_map()
        elif response == "Exit to Menu":
            state_of_game = GameState.MENU
        elif response is None:
            saving = False

    pygame.display.flip()
