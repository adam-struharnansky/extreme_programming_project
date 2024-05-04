import os.path
from dataclasses import dataclass

from source.game.characters import Creature


@dataclass(eq=True)
class Player(Creature):
    name: str = ""
    level: int = 0
    current_experience: int = 0
    next_level_experience: int = 2

    _picture_path: str = os.path.join('creatures', 'base_player.png')

    def change_experience(self, experience_change: int) -> None:
        self.current_experience += experience_change
        self.update_level()

    def update_level(self) -> None:
        while self.current_experience >= self.next_level_experience:
            self.level += 1
            self.current_experience -= self.next_level_experience
            self.next_level_experience = self.get_next_next_level_experience()

    def get_next_next_level_experience(self) -> int:
        return int(self.next_level_experience * 1.5)  # todo: Balance this constant (or change this function entirely)

    @property
    def picture_path(self) -> str:
        return self._picture_path
