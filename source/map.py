import os
import pickle
import pygame
import random

from auxiliary.enums import Key
from auxiliary.colors import *
from field import Field
from player import Player


FIELD_SIZE = 135
OFFSET = 2
ABS_PATH = os.path.dirname(os.path.dirname(__file__))


class Map:
    class Data:
        def __init__(self):
            self.map = None
            # todo: Odstranit field_size a namiesto toto pouzivat FIELD_SIZE. Treba pritom zmenit verziu pickle suborov!
            self.field_size = 135
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
            map_number = len(os.listdir('../data'))
            file = f'data/map{map_number}.pickle'
        with open(file, 'wb') as f:
            pickle.dump(self._dat, f)

    def load_map(self, file: str = None) -> None:
        if file is None:
            file = self._file
        with open(file, 'rb') as f:
            self._dat = pickle.load(f)

    def generate_enemies(self, row_number: int = 100, column_number: int = 100) -> None:
        # todo: Pridat generovanie nepriatelov
        # todo: Pridat ich ulozenie do self._dat (vyriesit ako, zmenit verziu .pickle suborov)
        # todo: Porozmyslat, ako sa to ma generovat, ci chceme aby loot aj nepriatelia boli na tych istych miestach
        pass

    def generate_loot(self, row_number: int = 100, column_number: int = 100) -> None:
        # todo: Pridat generovanie loot-u
        # todo: Pridat ich olozenie do self.dat (vyriesit ako, zmenit verziu .pickle suborov)
        pass

    def generate_map(self, row_number: int = 100, column_number: int = 100) -> None:
        self._dat = self.Data()
        self._dat.map = [[Field() for _ in range(column_number)] for _ in range(row_number)]
        self._dat.player = Player()
        self._dat.player_pos = [random.randint(0, row_number - 1), random.randint(0, column_number - 1)]
        self.generate_enemies(row_number, column_number)
        self.generate_loot(row_number, column_number)

    def move_player_if_possible(self, row, column):
        # todo: Pridat logiku aby Player nemohol ist do Water, Mountain (pripadne zatiahnut sem aj efekty?)
        if 0 <= row < len(self._dat.map) and 0 <= column < len(self._dat.map[0]):
            self._dat.player_pos[0] = row
            self._dat.player_pos[1] = column

    def move(self, direction: int) -> None:
        match direction:
            case Key.RIGHT.value:
                self.move_player_if_possible(self._dat.player_pos[0], self._dat.player_pos[1] + 1)
            case Key.LEFT.value:
                self.move_player_if_possible(self._dat.player_pos[0], self._dat.player_pos[1] - 1)
            case Key.DOWN.value:
                self.move_player_if_possible(self._dat.player_pos[0] + 1, self._dat.player_pos[1])
            case Key.UP.value:
                self.move_player_if_possible(self._dat.player_pos[0] - 1, self._dat.player_pos[1])
        if self.DEBUG:
            print('map._dat.player_pos', self._dat.player_pos)

    def draw(self):
        self._screen.fill(self._background_color)
        self.draw_map()
        self.draw_enemies()
        self.draw_player()
        self.draw_statistics()

    def draw_statistics(self):
        text = ""
        text += "Att: " + str(self._dat.player.get_real_attack())
        text += " | Def: " + str(self._dat.player.get_real_defence())
        text += " | Evs: " + str(self._dat.player.evasion)
        text += " | Spd: " + str(self._dat.player.speed)
        text += " | Lvl: " + str(self._dat.player.level)
        text += " | XP: " + str(self._dat.player.defence) + "/" + str(
            self._dat.player.next_level_experience)
        text += " | HP: " + str(self._dat.player.health) + "/" + str(self._dat.player.max_health)

        text_surface = self._font.render(text, False, WHITE)
        self._stat_tab.fill(BLACK)
        self._stat_tab.blit(text_surface, (10, 5))

    def draw_player(self):
        x = 2 * (FIELD_SIZE + 5)
        y = 2 * (FIELD_SIZE + 5)
        # drawing base player
        image = pygame.image.load(ABS_PATH+"//"+self._dat.player.picture_path)
        self._screen.blit(image, (x, y))
        # drawing armory on top of the base player
        for armor in self._dat.player.get_equipment():
            if armor:
                self._screen.blit(pygame.image.load(ABS_PATH+"//"+armor.picture_path), (x, y))

    def draw_enemies(self):
        for row_number, row in enumerate(self._dat.map):
            for column_number, field in enumerate(row):
                if field.enemy_present:
                    y = (FIELD_SIZE + 5) * row_number
                    x = (FIELD_SIZE + 5) * column_number
                    # todo: Vykreslit nepriatela
                    # todo: Vykreslit aj vsetku zbroj nepriatela (ak im ju chceme pridat)

    def draw_map(self):
        for row_difference in range(-OFFSET, OFFSET + 1):
            for column_difference in range(-OFFSET, OFFSET + 1):
                row = self._dat.player_pos[0] + row_difference
                column = self._dat.player_pos[1] + column_difference
                if 0 <= row < len(self._dat.map) and 0 <= column < len(self._dat.map):
                    x = (FIELD_SIZE + 5) * (column_difference + OFFSET)
                    y = (FIELD_SIZE + 5) * (row_difference + OFFSET)
                    field = self._dat.map[row][column]
                    image = pygame.image.load(ABS_PATH+"//"+field.picture_path)
                    self._screen.blit(image, (x, y))
