import os
import pickle
import pygame
import random

import colors
from enums import Key, ArmorType
from colors import *
from field import Field
from player import Player


class Map:
    class Data:
        def __init__(self):
            self.map = None
            self.field_size = 135  # toto presunut, myslim ze toto uz nebudeme moct menit v dalsich verziach
            self.player_pos = [0, 0]  # row column
            self.player = Player()

    def __init__(self, screen: pygame.Surface,
                 stat_tab: pygame.Surface,
                 file: str = 'data/map2.pickle',
                 debug: bool = False) -> None:
        self._dat = self.Data()
        self._screen = screen
        self._stat_tab = stat_tab
        self._file = file
        pygame.font.init()
        self._font = pygame.font.SysFont('Arial', 30)
        self._background_color = WHITE
        self.DEBUG = debug

    def save_map(self, file: str = None) -> None:
        """
        Save this map to the file specified in the str. If no file name provided, the map will be stored at
        data/mapXX.pickle, where XX marks the new generated map number
        :param file: Name of the file where map should be stored
        """
        if file is None:
            map_number = len(os.listdir('data'))
            file = f'data/map{map_number}.pickle'
        with open(file, 'wb') as f:
            pickle.dump(self._dat, f)

    def load_map(self, file: str = None) -> None:
        if file is None:
            file = self._file
        with open(file, 'rb') as f:
            self._dat = pickle.load(f)

    def generate_enemies(self, row_number, column_number):
        for x, row in enumerate(self._dat.map):
            for y, field in enumerate(row):
                # todo - pridat generovanie nepriatelov
                # todo - pridat ich ulozenie do self._dat (vyriesit ako, zmenit verziu .pickle suborov)
                # todo - porozmyslat, ako sa to ma generovat, ci chceme aby loot aj nepriatelia boli na tych istych miestach
                pass

    def generate_loot(self, row_number, column_number):
        for x, row in enumerate(self._dat.map):
            for y, field in enumerate(row):
                pass  # todo

    def generate_map(self, row_number: int = 100, column_number: int = 100):
        self._dat = self.Data()
        self._dat.map = [[Field() for _ in range(column_number)] for _ in range(row_number)]
        self._dat.player = Player()
        self._dat.player_pos = [random.randint(0, row_number - 1), random.randint(0, column_number - 1)]
        self.generate_enemies(row_number, column_number)
        self.generate_loot(row_number, column_number)

    def move(self, direction):
        match direction:
            case Key.RIGHT.value:
                self._dat.player_pos[0] += 1
                self._dat.player_pos[0] = min(len(self._dat.map) - 1, self._dat.player_pos[0])
            case Key.LEFT.value:
                self._dat.player_pos[0] -= 1
                self._dat.player_pos[0] = max(0, self._dat.player_pos[0])
            case Key.DOWN.value:
                self._dat.player_pos[1] += 1
                self._dat.player_pos[1] = min(len(self._dat.map[0]) - 1, self._dat.player_pos[1])
            case Key.UP.value:
                self._dat.player_pos[1] -= 1
        self._dat.player_pos[1] = max(0, self._dat.player_pos[1])
        if self.DEBUG:
            print("Player pos:", self._dat.player_pos)

    def draw(self):
        self._screen.fill(self._background_color)
        self.draw_map()
        self.draw_enemies()
        self.draw_player()
        self.draw_statistics()

    def draw_statistics(self):
        text = ""
        text += "Att: " + str(self._dat.player.get_attack())
        text += " | Def: " + str(self._dat.player.get_defence())
        text += " | Evs: " + str(self._dat.player.get_evasion())
        text += " | Spd: " + str(self._dat.player.get_speed())
        text += " | Lvl: " + str(self._dat.player.get_level())
        text += " | XP: " + str(self._dat.player.get_defence()) + "/" + str(
            self._dat.player.get_next_level_experience())
        text += " | HP: " + str(self._dat.player.get_health()) + "/" + str(self._dat.player.get_max_health())
        text_surface = self._font.render(text, False, WHITE)
        self._stat_tab.blit(text_surface, (10, 5))

    def draw_player(self):

        field_size = self._dat.field_size

        center_x = 2 * (field_size + 5)
        center_y = 2 * (field_size + 5)

        image_path = os.path.join("graphics", "base_player.png")
        image = pygame.image.load(image_path)
        self._screen.blit(image, (center_x, center_y))
        for armor in self._dat.player.get_equipment():
            if armor:
                image = pygame.image.load(armor.get_picture_path())
                self._screen.blit(image, (center_x, center_y))

    def draw_enemies(self):
        field_size = self._dat.field_size
        for x, row in enumerate(self._dat.map):
            for y, field in enumerate(row):
                if field.is_enemy_present():
                    center_x = x * (field_size + 5)
                    center_y = y * (field_size + 5)

                    image_path = os.path.join("graphics", "base_enemy.png")
                    image = pygame.image.load(image_path)
                    self._screen.blit(image, (center_x, center_y))

                    # todo - vykreslit aj vsetku zbroj nepriatela (ak im ju chceme pridat)

    def draw_map(self):

        field_size = self._dat.field_size
        px, py = self._dat.player_pos
        for x, row in enumerate(self._dat.map[max(px - 2, 0):px + 3]):
            for y, field in enumerate(row[max(py - 2, 0):py + 3]):
                # color = self.colors.get(field.field_type, (0, 0, 0))
                color = colors.get_field_color(field.get_field_type())

                adjusted_x, adjusted_y = x, y
                adjusted_x -= min(px - 2, 0)
                adjusted_y -= min(py - 2, 0)
                pygame.draw.rect(self._screen, color, (adjusted_x * (field_size + 5),
                                                      adjusted_y * (field_size + 5),
                                                      field_size,
                                                      field_size))
