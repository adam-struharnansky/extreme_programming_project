from creature import Creature


class Player(Creature):

    def __init__(self,
                 health=0,
                 attack=0,
                 defence=0,
                 evasion=0,
                 equipment=None,
                 inventory=None,
                 effects=None,
                 name="",
                 level=0,
                 current_experience=0,
                 next_level_experience=0):

        super().__init__(health, attack, defence, evasion, equipment, inventory, effects)
        self._name = name
        self._level = level
        self._current_experience = current_experience
        self._next_level_experience = next_level_experience

    def get_level(self):
        return self._level

    def change_experience(self, experience_change):
        self._current_experience += experience_change
        self.update_level()

    def update_level(self):
        while self._current_experience >= self._next_level_experience:
            self._level += 1
            self._current_experience -= self._next_level_experience
            self._next_level_experience = self.get_next_next_level_experience(self._next_level_experience)

    def get_next_next_level_experience(self, current_next_level_experience):
        return current_next_level_experience * 1.5  # todo - vybalansovat tuto konstantu
