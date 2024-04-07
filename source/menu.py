import pygame
from buttons import Button

class CheckboxGroup:
    def __init__(self):
        self.checkboxes = []
    
    def add(self, checkbox):
        self.checkboxes.append(checkbox)
        checkbox.group = self
        
    def handle_event(self, event, checkbox):
        # If a checkbox is clicked, uncheck all others in the group
        if checkbox.is_checked:
            for cb in self.checkboxes:
                if cb != checkbox:
                    cb.is_checked = False

class CheckBox:
    def __init__(self, x, y, width, height, text, screen, font=None, is_checked=False, option=None):
        self.x = x
        self.y = y
        self.width = width  # Width of the clickable area, not the text
        self.height = height
        self.text = text
        self.screen = screen
        self.is_checked = is_checked
        self.font = font if font else pygame.font.Font(None, 32)
        self.text_surface = self.font.render(text, True, (0, 0, 0))
        # Keep the box as the clickable area, which is exactly 50x50 pixels for the box
        self.box = pygame.Rect(x, y, width, height)
        self.option = option
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.box.collidepoint(event.pos):
                # Toggle the checkbox state if the box area is clicked
                self.is_checked = not self.is_checked
                # Notify the group (if part of one) about the state change
                if self.group:
                    self.group.handle_event(event, self)

    def draw(self):
        # If checked, draw an "X", otherwise just draw the box
        if self.is_checked:
            pygame.draw.rect(self.screen, (255, 255, 255), self.box)
            pygame.draw.rect(self.screen, (0, 0, 0), self.box, 2)  # Border for box
            center = self.box.center
            pygame.draw.line(self.screen, (255, 0, 0), (center[0] - 10, center[1] - 10), (center[0] + 10, center[1] + 10), 3)
            pygame.draw.line(self.screen, (255, 0, 0), (center[0] + 10, center[1] - 10), (center[0] - 10, center[1] + 10), 3)
        else:
            # Draw the white box with a black border
            pygame.draw.rect(self.screen, (255, 255, 255), self.box)
            pygame.draw.rect(self.screen, (0, 0, 0), self.box, 2)  # Border for box

        # Draw the text next to the box
        self.screen.blit(self.text_surface, (self.x + self.width + 10, self.y + (self.height - self.text_surface.get_height()) // 2))


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
        # You might choose to use different groups for different sets of options
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
        # Assuming you have a font and color defined for your Menu class
        label_font = pygame.font.Font(None, 36)  # Create a font object. None means default font, size 36
        label_color = (0, 0, 0)  # Color white
        
        # Render "Biome Size" text label before drawing biome size checkboxes
        biome_label_text = "select biome type"
        biome_label_surface = label_font.render(biome_label_text, True, label_color)  # True for antialiased text
        biome_label_position = (200, 10)  # Adjust this to position your label correctly
        self.screen.blit(biome_label_surface, biome_label_position)

         # Render "Biome Size" text label before drawing biome size checkboxes
        map_label_text = "select map size"
        map_label_surface = label_font.render(map_label_text, True, label_color)  # True for antialiased text
        map_label_position = (200, 260)  # Adjust this to position your label correctly
        self.screen.blit(map_label_surface, map_label_position)
        
        # Draw existing size option buttons
        for button in self.menu_buttons:
            button.draw()




    def handle_event(self, event):


        # New: Event handling for checkboxes
        for checkbox in self.menu_buttons:
            checkbox.handle_event(event)

            clock = pygame.time.Clock()

