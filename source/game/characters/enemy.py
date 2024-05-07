
import os
from dataclasses import dataclass

from source.game.characters import Creature


@dataclass
class Enemy(Creature):
    name: str = ""
    description: str = ""
    experience_drop: int = 0

    def __post_init__(self):
        self._picture_path = os.path.join('creatures', 'base_enemy.png')

    @property
    def picture_path(self) -> str:
        """
        Overriding Creature function
        """
        return self._picture_path

    def generate_random_properties(self):
        pass
        # todo: Generate random enemy
