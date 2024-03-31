import pygame
import sys

from enum import Enum
from field import Field
from map import Map
from menu import Menu


class GameState(Enum):
    MENU = 0
    LOADING_GAME = 1


# Initialize Pygame
pygame.init()

# Set the size of the window and create it
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption('Pygame Basic Window')

# Set a background color
background_color = (255, 255, 255) # RGB color for white
##############################################################################################


############################################################################################
#Tu budu premenne ktore potrebujeme mat v hlavnom cykle

#state_of_game premenna sluzi nato aby sme vedeli v akom bude hry sa nachadzame, 0-zakladne menu
state_of_game = GameState.MENU
buttons = []

#tu bude zadefinovanie classes ak je potrebne
menu = Menu(buttons, screen)
map = Map(screen)





# Main loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    buttons = []
    screen.fill(background_color)

    #Spravanie ak sme v menu state_of_game = 0
    if state_of_game == GameState.MENU:
        menu.create_base_menu()

        buttons = menu.buttons

        for button in buttons:
            temp_response = button.handle_event(event)
            if temp_response != None:
               response = temp_response
               break
        else:
            response = None

        #Kliknutie na button load Game a zmenenie stavu
        if response in ["Load Game", "New Game"]:
            state_of_game = GameState.LOADING_GAME

    #Nacitanie mapy
    if state_of_game == GameState.LOADING_GAME:
        map.load_map()

    # Fill the screen with the background color
    

    # Update the display
    pygame.display.flip()
