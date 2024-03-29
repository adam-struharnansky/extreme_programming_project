from creature import Creature


class Enemy(Creature):

    def __init__(self,
                 health=0,
                 attack=0,
                 defence=0,
                 evasion=0,
                 equipment=None,
                 inventory=None,
                 effects=None,
                 name="",
                 description="",
                 experience_drop=0):

        super().__init__(health, attack, defence, evasion, equipment, inventory, effects)
        self._name = name
        self._description = description
        self._experience_drop = experience_drop

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_experience_drop(self):
        return self._experience_drop
