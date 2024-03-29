import pygame
import sys
from menu import Menu
from field import Field
from map import Map

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
state_of_game = 0
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
    if state_of_game == 0:
        menu.create_base_menu()

        buttons = menu.buttons

        for button in buttons:
           response =  button.handle_event(event)

        #Kliknutie na button load Game a zmenenie stavu
        if response == "Load Game"  or response == "New Game":
            state_of_game = 1

    #Nacitanie mapy
    if state_of_game == 1:
        map.load_map()

    # Fill the screen with the background color
    

    # Update the display
    pygame.display.flip()
