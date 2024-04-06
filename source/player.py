import os.path

from creature import Creature


class Player(Creature):

    def __init__(self,
                 health: int = 10,
                 max_health: int = 10,
                 attack: int = 0,
                 defence: int = 0,
                 evasion: int = 0,
                 speed: int = 0,
                 equipment: list = None,
                 inventory: list = None,
                 effects: list = None,
                 name: str = "",
                 level: int = 0,
                 current_experience: int = 0,
                 next_level_experience: int = 2):

        super().__init__(health, max_health, attack, defence, evasion, speed, equipment, inventory, effects)
        self._name = name
        self._level = level
        self._current_experience = current_experience
        self._next_level_experience = next_level_experience
        self._picture_path = os.path.join('graphics', 'creatures', 'base_player.png')

    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, Player):
            return False
        if self._health != other.health:
            return False
        if self._max_health != other.max_health:
            return False
        if self._attack != other.attack:
            return False
        if self._defence != other.defence:
            return False
        if self._evasion != other.evasion:
            return False
        if self._speed != other.speed:
            return False
        if self._equipment != other.get_equipment():
            return False
        if self._inventory != other.inventory:
            return False
        if self._effects != other.effects:
            return False
        if self._name != other.name:
            return False
        if self._level != other.level:
            return False
        if self._current_experience != other.current_experience:
            return False
        if self._next_level_experience != other.next_level_experience:
            return False
        return True

    @property
    def name(self):
        return self._name

    @property
    def current_experience(self):
        return self._current_experience

    def change_experience(self, experience_change: int) -> None:
        self._current_experience += experience_change
        self.update_level()

    def update_level(self) -> None:
        while self._current_experience >= self._next_level_experience:
            self._level += 1
            self._current_experience -= self._next_level_experience
            self._next_level_experience = self.get_next_next_level_experience()

    @property
    def level(self) -> int:
        return self._level

    @property
    def next_level_experience(self) -> int:
        return self._next_level_experience

    def get_next_next_level_experience(self) -> int:
        return int(self._next_level_experience * 1.5)  # todo - vybalansovat tuto konstantu

    @property
    def picture_path(self) -> str:
        """
        Overriding Creature function
        """
        return self._picture_path
