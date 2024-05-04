
import os
from dataclasses import dataclass

from source.game.characters import Creature


@dataclass
class Enemy(Creature):
    name: str = ""
    description: str = ""
    experience_drop: int = 0

    def picture_path(self) -> str:
        """
        Overriding Creature function
        """
        return os.path.join('creatures', 'base_enemy.png')

    def generate_random_properties(self):
        pass
        # todo: Generate random enemy