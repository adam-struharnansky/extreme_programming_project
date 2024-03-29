import pygame
from buttons import Button



class Menu:

    def __init__(self, buttons, screen):
        info = pygame.display.Info()

        self.screen = screen

        self.buttons = buttons
        self.width_of_screen = info.current_w
        self.height_of_screen = info.current_h

    def create_base_menu(self):
        
        new_game = Button(200, 400,  400, 50, "New Game", self.screen)

        load_game = Button(200, 500, 400, 50, "Load Game", self.screen)

        self.buttons.append(new_game)
        self.buttons.append(load_game)

        new_game.draw()
        load_game.draw()
