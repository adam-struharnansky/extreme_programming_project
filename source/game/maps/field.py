import logging
import os.path
import random

from dataclasses import dataclass, field
from typing import Dict, Optional

from source.auxiliary import FieldType
from source.game.characters import Enemy
from source.game.items import Loot


@dataclass(eq=True)
class Field:
    field_type: FieldType = field(default_factory=lambda: random.choice(list(FieldType)))
    properties: Dict[str, any] = field(default_factory=dict)
    enemy: Optional[Enemy] = None
    loot: Optional[Loot] = None

    def __post_init__(self):
        match self.field_type:
            case FieldType.WATER:
                self._picture_path = os.path.join('map_tiles', 'water.png')
            case FieldType.FOREST:
                self._picture_path = os.path.join('map_tiles', 'forest.png')
            case FieldType.MOUNTAIN:
                self._picture_path = os.path.join('map_tiles', 'mountain.png')
            case FieldType.PLAINS:
                self._picture_path = os.path.join('map_tiles', 'plains.png')
            case FieldType.DESERT:
                self._picture_path = os.path.join('map_tiles', 'desert.png')
            case _:
                logging.error('Non existent FieldType for Field initialization')
                self._picture_path = os.path.join('graphics', 'error', 'empty.png')

    @property
    def picture_path(self):
        return self._picture_path
