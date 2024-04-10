import pygame

from source.auxiliary.colors import BLACK
from source.front_end.buttons import Button
from source.front_end.check_box import CheckBox
from source.front_end.checkbox_group import CheckboxGroup


class Menu:

    def __init__(self, screen):
        info = pygame.display.Info()

        self._screen = screen
        self._base_menu_buttons = []
        self._in_game_buttons = []
        self._lost_game_buttons = []
        self._menu_buttons = []
        self._width_of_screen = info.current_w  # todo: Potrebujeme si toto ukladat?
        self._height_of_screen = info.current_h  # todo: Potrebujeme si toto ukladat?
        self._map_sizes_group = CheckboxGroup()
        self._map_biomes_group = CheckboxGroup()

        self._create_base_menu()
        self._create_in_game_menu()
        self._create_lost_game_menu()
        self._create_size_options()

    def _create_base_menu(self):
        new_game = Button(150, 500, 400, 50, "New Game", self._screen)
        load_game = Button(150, 600, 400, 50, "Load Game", self._screen)
        exit_game = Button(150, 700, 400, 50, "Exit Game", self._screen)

        self._base_menu_buttons.append(new_game)
        self._base_menu_buttons.append(load_game)
        self._base_menu_buttons.append(exit_game)

    def draw_base_menu(self):
        for button in self._base_menu_buttons:
            button.draw()

    def _create_in_game_menu(self):
        save_game = Button(0, 750, 350, 20, "Save Game", self._screen)
        exit_to_menu = Button(350, 750, 350, 20, "Exit to Menu", self._screen)

        self._in_game_buttons.append(save_game)
        self._in_game_buttons.append(exit_to_menu)

    def draw_in_game_buttons(self):
        for button in self._in_game_buttons:
            button.draw()

    def _create_lost_game_menu(self):
        exit_to_menu = Button(150, 300, 400, 50, "Main menu", self._screen)
        self._lost_game_buttons.append(exit_to_menu)

    def draw_lost_game_buttons(self):
        for button in self._lost_game_buttons:
            button.draw()

    def _create_size_options(self):
        map_sizes = [[50, 50], [100, 100], [200, 200]]
        biome_options = ['Random map', 'Biomes map', 'Large Biomes map']
        offset_y = 0

        for size, option in zip(map_sizes, biome_options):
            map_size_check_box = CheckBox(320, 300 + offset_y, 50, 50, f'W: {size[0]}, H:{size[1]}', self._screen,
                                          option={'label': 'sizes',
                                                  'value': {'row_number': size[0], 'column_number': size[1]}})
            map_type_check_box = CheckBox(320, 50 + offset_y, 50, 50, option, self._screen,
                                          option={'label': 'biome_type', 'value': option})

            self._menu_buttons.append(map_size_check_box)  # todo: Toto su button-y alebo checkbox-y?
            self._menu_buttons.append(map_type_check_box)  # todo: Toto su button-y alebo checkbox-y?

            self._map_sizes_group.add(map_size_check_box)
            self._map_biomes_group.add(map_type_check_box)
            offset_y += 70

    def draw_size_options(self):
        label_font = pygame.font.Font(None, 36)
        label_color = BLACK

        biome_label_text = "select biome type"
        biome_label_surface = label_font.render(biome_label_text, True, label_color)
        biome_label_position = (200, 10)
        self._screen.blit(biome_label_surface, biome_label_position)

        map_label_text = "select map size"
        map_label_surface = label_font.render(map_label_text, True, label_color)
        map_label_position = (200, 260)
        self._screen.blit(map_label_surface, map_label_position)

        for button in self._menu_buttons:
            button.draw()

    def handle_event(self, event):

        for checkbox in self._menu_buttons:
            checkbox.handle_event(event)
            clock = pygame.time.Clock()  # todo: Naco sa tu vytvara ta premenna clock? Nestaci iba zavolat pravu cast?

    @property
    def lost_game_buttons(self):
        return self._lost_game_buttons

    @property
    def menu_buttons(self):
        return self._menu_buttons

    @property
    def in_game_buttons(self):
        return self._in_game_buttons

    @property
    def base_menu_buttons(self):
        return self._base_menu_buttons
