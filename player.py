from creature import Creature


class Player(Creature):

    def __init__(self,
                 health:int=0,
                 max_health:int=1,
                 attack:int=0,
                 defence:int=0,
                 evasion:int=0,
                 speed: int = 0,
                 equipment:list=None,
                 inventory:list=None,
                 effects:list=None,
                 name:str="",
                 level:int=0,
                 current_experience:int=0,
                 next_level_experience:int=2):

        super().__init__(health, max_health, attack, defence, evasion, speed, equipment, inventory, effects)
        self._name = name
        self._level = level
        self._current_experience = current_experience
        self._next_level_experience = next_level_experience

    def __eq__(self, other):
        if self._health != other._health:
            return False
        if self._max_health != other._max_health:
            return False
        if self._attack != other._attack:
            return False
        if self._defence != other._defence:
            return False
        if self._evasion != other._evasion:
            return False
        if self._speed != other._speed:
            return False
        if self._equipment != other._equipment:
            return False
        if self._inventory != other._inventory:
            return False
        if self._effects != other._effects:
            return False
        if self._name != other._name:
            return False
        if self._level != other._level:
            return False
        if self._current_experience != other._current_experience:
            return False
        if self._next_level_experience != other._next_level_experience:
            return False

        return True

    def get_level(self) -> int:
        return self._level

    def change_experience(self, experience_change:int) -> None:
        self._current_experience += experience_change
        self.update_level()

    def update_level(self) -> None:
        while self._current_experience >= self._next_level_experience:
            self._level += 1
            self._current_experience -= self._next_level_experience
            self._next_level_experience = self.get_next_next_level_experience(self._next_level_experience)

    def get_next_level_experience(self) -> int:
        return self._next_level_experience

    def get_next_next_level_experience(self, current_next_level_experience:int) -> int:
        return current_next_level_experience * 1.5  # todo - vybalansovat tuto konstantu
