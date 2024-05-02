import os
import pickle
import random

import pygame

from source.auxiliary import BLACK, WHITE
from source.auxiliary import GRAPHIC_DIRECTORY, DATA_DIRECTORY
from source.auxiliary import Key, FieldType
from source.game.characters import Enemy
from source.game.characters import Player
from source.game.maps import Field
from source.game.maps import Map

FIELD_SIZE = 135
OFFSET = 2
NOT_ACCESSIBLE_FIELDS = [FieldType.WATER, FieldType.MOUNTAIN]

class MockMap(Map):
    def generate_random_map(self, row_count: int = 100, column_count: int = 100) -> None:
        self.load_map()
