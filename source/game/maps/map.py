import os
import pickle
import random

import logging
import pygame

from source.auxiliary import BLACK, WHITE
from source.auxiliary import GRAPHIC_DIRECTORY, DATA_DIRECTORY
from source.auxiliary import Direction, FieldType, MapType
from source.game.characters import Enemy
from source.game.characters import Player
from source.game.maps import Field

FIELD_SIZE = 135
OFFSET = 2
NOT_ACCESSIBLE_FIELDS = [FieldType.WATER, FieldType.MOUNTAIN]


class Map:
    class Data:
        def __init__(self):
            self.map = None
            self.version = 1
            self.player_pos = [0, 0]  # row column
            self.player = Player()

    def __init__(self, screen: pygame.Surface,
                 stat_tab: pygame.Surface,
                 file: str = 'map2.pickle',
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
        logging.info('Saving the map')
        if file is None:
            map_number = len(os.listdir(DATA_DIRECTORY))
            file = f'map{map_number}.pickle'
        with open(os.path.join(DATA_DIRECTORY, file), 'wb') as f:
            pickle.dump(self._dat, f)

    def load_map(self, file: str = None) -> None:
        if file is None:
            file = self._file
        with open(os.path.join(DATA_DIRECTORY, file), 'rb') as f:
            self._dat = pickle.load(f)
        expected_version = self.Data().version
        if not hasattr(self._dat, 'version') or self._dat.version != expected_version:
            raise ValueError("Mismatched pickle file version for map")

    def generate_enemies(self, spawn_chance=0.05) -> None:
        for row in self._dat.map:
            for field in row:
                if random.random() < spawn_chance and field.field_type not in NOT_ACCESSIBLE_FIELDS:
                    field.enemy = Enemy()
                    field.enemy.generate_random_properties()

    def generate_loot(self, spawn_chance=0.05) -> None:
        for row in self._dat.map:
            for field in row:
                if random.random() < spawn_chance and field.field_type not in NOT_ACCESSIBLE_FIELDS:
                    if field.enemy is None:  # loot and enemy can not be at the same place
                        # field.add_active_object()  # todo: Add loot generation
                        pass

    def _spread_terrain(self, start_row, start_col, field_type, row_count, column_count, spread_chance=0.5,
                        spread_steps=3):
        if spread_steps == 0:
            return
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                new_row, new_col = start_row + d_row, start_col + d_col
                if 0 <= new_row < row_count and 0 <= new_col < column_count:
                    if random.random() < spread_chance:
                        self._dat.map[new_row][new_col] = Field(field_type)
                        self._spread_terrain(new_row, new_col, field_type, spread_chance * 0.9, spread_steps - 1)

    def _place_player_randomly(self, row_count: int = 50, column_count: int = 50):
        while True:
            row, col = random.randint(0, row_count - 1), random.randint(0, column_count - 1)
            if self._dat.map[row][col].field_type != FieldType.WATER \
                    and self._dat.map[row][col].field_type != FieldType.MOUNTAIN:
                self._dat.player = Player()
                self._dat.player_pos = [row, col]
                break

    def generate_biomes_map(self, row_count: int = 50, column_count: int = 50, biome_count: int = 5):
        self._dat = self.Data()
        self._dat.map = [[Field(FieldType.PLAINS) for _ in range(column_count)] for _ in range(row_count)]

        for field_type in FieldType:
            num_seeds = random.randint(int(biome_count - biome_count * 0.2), int(biome_count + biome_count * 0.2))
            for _ in range(num_seeds):
                seed_row = random.randint(num_seeds, row_count - 1)
                seed_col = random.randint(num_seeds, column_count - 1)
                self._spread_terrain(seed_row, seed_col, field_type, row_count, column_count)

        self._place_player_randomly()
        self.generate_enemies()
        self.generate_loot()

    def generate_random_map(self, row_count: int = 100, column_count: int = 100) -> None:
        self._dat = self.Data()
        self._dat.map = [[Field() for _ in range(column_count)] for _ in range(row_count)]
        self._place_player_randomly()
        self.generate_enemies()
        self.generate_loot()

    def generate_map(self, row_count: int = 50, column_count: int = 50, map_type: MapType = MapType.RANDOM):
        match map_type.value:
            case MapType.RANDOM.value:
                self.generate_random_map(row_count, column_count)
            case MapType.SMALL_BIOMES.value:
                self.generate_biomes_map(row_count, column_count, 5)
            case MapType.LARGE_BIOMES.value:
                self.generate_biomes_map(row_count, column_count, 15)
            case _:
                raise ValueError('Not supported map type')

    def move_player_if_possible(self, row, column):
        if 0 <= row < len(self._dat.map) and 0 <= column < len(self._dat.map[0]) \
                and self._dat.map[row][column].field_type not in NOT_ACCESSIBLE_FIELDS:
            self._dat.player_pos[0] = row
            self._dat.player_pos[1] = column

    def move(self, direction: Direction) -> None:
        match direction.value:
            case Direction.RIGHT.value:
                self.move_player_if_possible(self._dat.player_pos[0], self._dat.player_pos[1] + 1)
            case Direction.LEFT.value:
                self.move_player_if_possible(self._dat.player_pos[0], self._dat.player_pos[1] - 1)
            case Direction.DOWN.value:
                self.move_player_if_possible(self._dat.player_pos[0] + 1, self._dat.player_pos[1])
            case Direction.UP.value:
                self.move_player_if_possible(self._dat.player_pos[0] - 1, self._dat.player_pos[1])
            case _:
                logging.warning(f'Not correct direction for move: {direction}')
        logging.debug(f'map._dat.player_pos{self._dat.player_pos}')

    def draw(self):
        self._screen.fill(self._background_color)
        self._draw_map()
        self._draw_player()
        self._draw_statistics()

    def _draw_statistics(self):
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

    def _draw_player(self):
        x = 2 * (FIELD_SIZE + 5)
        y = 2 * (FIELD_SIZE + 5)
        # drawing base player
        image = pygame.image.load(os.path.join(GRAPHIC_DIRECTORY, self._dat.player.picture_path))
        self._screen.blit(image, (x, y))
        # drawing armory on top of the base player
        for armor in self._dat.player.get_equipment():
            if armor:
                self._screen.blit(pygame.image.load(os.path.join(GRAPHIC_DIRECTORY, armor.picture_path)), (x, y))

    def _draw_map(self):
        for row_difference in range(-OFFSET, OFFSET + 1):
            for column_difference in range(-OFFSET, OFFSET + 1):
                row = self._dat.player_pos[0] + row_difference
                column = self._dat.player_pos[1] + column_difference

                if 0 <= row < len(self._dat.map) and 0 <= column < len(self._dat.map):
                    x = (FIELD_SIZE + 5) * (column_difference + OFFSET)
                    y = (FIELD_SIZE + 5) * (row_difference + OFFSET)
                    field = self._dat.map[row][column]

                    field_image = pygame.image.load(os.path.join(GRAPHIC_DIRECTORY, field.picture_path))
                    self._screen.blit(field_image, (x, y))

                    if field.enemy:
                        enemy_image = pygame.image.load(os.path.join(GRAPHIC_DIRECTORY, field.enemy.picture_path()))
                        self._screen.blit(enemy_image, (x, y))
                        for armor in field.enemy.get_equipment():
                            if armor:
                                self._screen.blit(
                                    pygame.image.load(os.path.join(GRAPHIC_DIRECTORY, armor.picture_path)), (x, y))

                    for _ in field.active_objects:
                        pass  # todo: Draw objects

    def is_game_lost(self):
        return not self._dat.player.is_alive()
