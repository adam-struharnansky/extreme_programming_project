import pygame

from source.auxiliary import BLACK, WHITE
from source.auxiliary import MapType, MapSize, GameState
from source.front_end import Button, CheckBox, CheckboxGroup


def _find_response(buttons: list[Button], event: pygame.event.Event) -> GameState | None:
    for button in buttons:
        response = button.get_response_to_event(event)
        if response:
            return response
    return None


class Menu:

    def __init__(self, screen):
        self._screen: pygame.Surface = screen
        self._base_menu_buttons: list[Button] = []
        self._in_game_buttons: list[Button] = []
        self._lost_game_buttons: list[Button] = []

        self._map_sizes_group = CheckboxGroup()
        self._map_types_group = CheckboxGroup()

        self._create_base_menu()
        self._create_in_game_menu()
        self._create_lost_game_menu()
        self._create_size_options()

    def _create_base_menu(self) -> None:
        new_game_button = Button(150, 500, 400, 50, "New Game", self._screen, GameState.LOADING_NEW_GAME)
        load_game_button = Button(150, 600, 400, 50, "Load Game", self._screen, GameState.LOADING_EXISTING_GAME)
        exit_game_button = Button(150, 700, 400, 50, "Exit Game", self._screen, GameState.EXIT)

        self._base_menu_buttons.append(new_game_button)
        self._base_menu_buttons.append(load_game_button)
        self._base_menu_buttons.append(exit_game_button)

    def _create_in_game_menu(self) -> None:
        save_game = Button(0, 750, 350, 20, "Save Game", self._screen, GameState.SAVING_GAME)
        exit_to_menu = Button(350, 750, 350, 20, "Exit to Menu", self._screen, GameState.MENU_INITIALIZATION)

        self._in_game_buttons.append(save_game)
        self._in_game_buttons.append(exit_to_menu)

    def _create_lost_game_menu(self) -> None:
        exit_to_menu = Button(150, 300, 400, 50, "Main menu", self._screen, GameState.MENU_INITIALIZATION)
        self._lost_game_buttons.append(exit_to_menu)

    def _create_size_options(self) -> None:
        for i, map_size in enumerate(MapSize):
            map_size_check_box = CheckBox(320, 300 + i * 70, 50, 50,
                                          f'Size: {map_size.value}', self._screen, _option=map_size)
            self._map_sizes_group.add(map_size_check_box)
        for i, map_type in enumerate(MapType):
            map_type_check_box = CheckBox(320, 50 + i * 70, 50, 50,
                                          f'Type: {map_type.value}', self._screen, _option=map_type)
            self._map_types_group.add(map_type_check_box)

    def draw_base_menu(self) -> None:
        self._screen.fill(WHITE)
        for button in self._base_menu_buttons:
            button.draw_button()
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
        self._map_sizes_group.draw_checkbox_group()
        self._map_types_group.draw_checkbox_group()

    def draw_in_game_buttons(self) -> None:
        for button in self._in_game_buttons:
            button.draw_button()

    def draw_lost_game_buttons(self) -> None:
        for button in self._lost_game_buttons:
            button.draw_button()

    def recheck_map_checkboxes(self, event: pygame.event.Event) -> None:
        self._map_sizes_group.handle_event(event)
        self._map_types_group.handle_event(event)

    def base_menu_response(self, event: pygame.event.Event) -> GameState:
        return _find_response(self._base_menu_buttons, event) or GameState.MENU

    def in_game_response(self, event: pygame.event.Event) -> GameState:
        return _find_response(self._in_game_buttons, event) or GameState.PLAYING_GAME

    def lost_game_response(self, event: pygame.event.Event) -> GameState:
        return _find_response(self._lost_game_buttons, event) or GameState.LOST_GAME

    def map_size(self) -> MapSize:
        map_size = self._map_sizes_group.get_value()
        if map_size:
            return map_size
        return MapSize.DEFAULT

    def map_type(self) -> MapType:
        map_type = self._map_types_group.get_value()
        if map_type:
            return map_type
        return MapType.DEFAULT
