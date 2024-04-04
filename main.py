import pygame
import sys

from enum import Enum
from enums import Key
from map import Map
from menu import Menu


class GameState(Enum):
    MENU = 0
    LOADING_NEW_GAME = 1
    LOADING_EXISTING_GAME = 2
    PLAYING_GAME = 3


pygame.init()

size = width, height = 700, 770
screen = pygame.display.set_mode(size)

screen1_size = (width, 50)
screen2_size = (width, height - 50)

screen1 = pygame.Surface(screen1_size)
screen2 = pygame.Surface(screen2_size)

DEBUG_ALL = False
DEBUG_KEY = True
DEBUG_MOVE = True

pygame.display.set_caption('Pygame Basic Window')

background_color = (255, 255, 255)

state_of_game = GameState.MENU
key_states = {}  # left, right, up, down
saving = False

# tu bude zadefinovanie classes ak je potrebne
menu = Menu(screen)
map = Map(screen2, screen1, debug=DEBUG_ALL or DEBUG_MOVE)


def handle_keys():
    keys = pygame.key.get_pressed()
    screen.blit(screen1, (0, 0))
    screen.blit(screen2, (0, 50))

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
            map.move(i)
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


# Main loop

while True:
    for event in pygame.event.get():
        if DEBUG_ALL:
            if event.type != pygame.MOUSEMOTION:
                print("Event: " + str(event))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)

    # Spravanie ak sme v menu state_of_game = 0
    if state_of_game == GameState.MENU:
        menu.draw_base_menu()

        for button in menu.base_menu_buttons:
            temp_response = button.handle_event(event)
            if temp_response is not None:
                response = temp_response
                break
        else:
            response = None

        # Kliknutie na button load Game a zmenenie stavu
        if response == "New Game":
            state_of_game = GameState.LOADING_NEW_GAME
        elif response == "Load Game":
            state_of_game = GameState.LOADING_EXISTING_GAME
        elif response == "Exit Game":
            break

    # Nacitanie mapy
    if state_of_game == GameState.LOADING_NEW_GAME:
        map.generate_map()
        map.draw()
        state_of_game = GameState.PLAYING_GAME
    if state_of_game == GameState.LOADING_EXISTING_GAME:
        map.load_map()
        map.draw()
        state_of_game = GameState.PLAYING_GAME

    if state_of_game == GameState.PLAYING_GAME:
        handle_keys()
        map.draw()
        menu.draw_in_game_buttons()

        for button in menu.in_game_buttons:
            temp_response = button.handle_event(event)
            if temp_response is not None:
                response = temp_response
                break
        else:
            response = None

        if response == "Save Game" and not saving:
            print("Map saved")
            saving = True
            map.save_map()
        elif response == "Exit to Menu":
            state_of_game = GameState.MENU
        elif response is None:
            saving = False

    pygame.display.flip()
