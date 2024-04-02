import pygame
from buttons import Button



class Menu:

    def __init__(self, screen):
        info = pygame.display.Info()

        self.screen = screen
        self.base_menu_buttons = []
        self.in_game_buttons = []
        self.width_of_screen = info.current_w
        self.height_of_screen = info.current_h

        self.create_base_menu()
        self.create_in_game_menu()

    def create_base_menu(self):
        new_game = Button(150, 300,  400, 50, "New Game", self.screen)
        load_game = Button(150, 400, 400, 50, "Load Game", self.screen)
        exit_game = Button(150, 500, 400, 50, "Exit Game", self.screen)

        self.base_menu_buttons.append(new_game)
        self.base_menu_buttons.append(load_game)
        self.base_menu_buttons.append(exit_game)

    def draw_base_menu(self):
        for button in self.base_menu_buttons:
            button.draw()

    def create_in_game_menu(self):
        save_game = Button(0, 750, 350, 20, "Save Game", self.screen)
        exit_to_menu = Button(350, 750, 350, 20, "Exit to Menu", self.screen)

        self.in_game_buttons.append(save_game)
        self.in_game_buttons.append(exit_to_menu)

    def draw_in_game_buttons(self):
        for button in self.in_game_buttons:
            button.draw()
