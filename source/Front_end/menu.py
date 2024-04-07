import pygame
from buttons import Button
from .check_box import CheckBox
from .checkbox_group import CheckboxGroup

class Menu:

    def __init__(self, screen):
        info = pygame.display.Info()

        self.screen = screen
        self.base_menu_buttons = []
        self.in_game_buttons = []
        self.lost_game_buttons = []
        self.menu_buttons = []  
        self.width_of_screen = info.current_w
        self.height_of_screen = info.current_h
        self.map_sizes_group = CheckboxGroup()
        self.map_biomes_group = CheckboxGroup()

        self.create_base_menu()
        self.create_in_game_menu()
        self.create_lost_game_menu()
        self.create_size_options() 


    def create_base_menu(self):
        new_game = Button(150, 500,  400, 50, "New Game", self.screen)
        load_game = Button(150, 600, 400, 50, "Load Game", self.screen)
        exit_game = Button(150, 700, 400, 50, "Exit Game", self.screen)

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

    def create_lost_game_menu(self):
        exit_to_menu = Button(150, 300,  400, 50, "Main menu", self.screen)
        self.lost_game_buttons.append(exit_to_menu)

    def draw_lost_game_buttons(self):
        for button in self.lost_game_buttons:
            button.draw()

    def create_size_options(self):

        map_sizes = [[50,50], [100,100], [200,200]]
        biomese_options = ['Random map', 'Biomes map', 'Large Biomese map']
        offset_y = 0

        for size, option in zip(map_sizes,biomese_options):
            map_size_button = CheckBox(320, 300 + offset_y, 50, 50, f'W: {size[0]}, H:{size[1]}', self.screen, option={'label':'sizes', 'value': {'row_number':size[0], 'column_number': size[1]}})
            biomese_button = CheckBox(320, 50 + offset_y, 50, 50, option, self.screen, option={'label':'biomese_type', 'value': option})

            self.menu_buttons.append(map_size_button)
            self.menu_buttons.append(biomese_button)

            self.map_sizes_group.add(map_size_button) 
            self.map_biomes_group.add(biomese_button) 
            offset_y += 70

        

    def draw_size_options(self):
        label_font = pygame.font.Font(None, 36)  
        label_color = (0, 0, 0)  
        

        biome_label_text = "select biome type"
        biome_label_surface = label_font.render(biome_label_text, True, label_color)  
        biome_label_position = (200, 10)  
        self.screen.blit(biome_label_surface, biome_label_position)


        map_label_text = "select map size"
        map_label_surface = label_font.render(map_label_text, True, label_color)  
        map_label_position = (200, 260) 
        self.screen.blit(map_label_surface, map_label_position)
        

        for button in self.menu_buttons:
            button.draw()




    def handle_event(self, event):

        for checkbox in self.menu_buttons:
            checkbox.handle_event(event)

            clock = pygame.time.Clock()

