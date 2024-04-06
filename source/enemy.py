import os

from creature import Creature


class Enemy(Creature):

    def __init__(self,
                 health: int = 0,
                 max_health: int = 1,
                 attack: int = 0,
                 defence: int = 0,
                 evasion: int = 0,
                 speed: int = 0,
                 equipment: list = None,
                 inventory: list = None,
                 effects: list = None,
                 name: str = "",
                 description: str = "",
                 experience_drop: int = 0) -> None:
        super().__init__(health, max_health, attack, defence, evasion, speed, equipment, inventory, effects)
        self._name = name
        self._description = description
        self._experience_drop = experience_drop

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def experience_drop(self) -> int:
        return self._experience_drop

    def picture_path(self) -> str:
        """
        Overriding Creature function
        """
        return os.path.join('graphics', 'creatures', 'base_enemy.png')
