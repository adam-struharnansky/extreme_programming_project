
class Creature:
    def __init__(self,
                 health=0,
                 attack=0,
                 defence=0,
                 evasion=0,
                 equipment=None,
                 inventory=None,
                 effects=None):

        if effects is None:
            effects = []
        if inventory is None:
            inventory = []
        if equipment is None:
            equipment = []
        self._health = health
        self._attack = attack
        self._defence = defence
        self._evasion = evasion
        self._equipment = equipment
        self._inventory = inventory
        self._effects = effects

    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health

    def change_health(self, health_difference):
        self._health += health_difference

    def get_attack(self):
        return self._attack

    def set_attack(self, new_attack):
        self._attack = new_attack

    def get_real_attack(self):
        # todo + pridat aj z equipmentu
        return self.get_attack()

    def get_defence(self):
        return self._defence

    def set_defence(self, new_defence):
        self._defence = new_defence

    def get_evasion(self):
        return self._evasion

    def set_evasion(self, new_evasion):
        self._evasion = new_evasion

    def get_equipment(self):
        return self._equipment

    def add_item_equipment(self, item):
        # todo kontrola - nechceme mat naraz dva mece, atd
        self._equipment.append(item)
        return True  # podla toho, ci sa podarilo vlzoit, alebo nie

    def get_inventory(self):
        return self._inventory

    def add_item_inventory(self, item):
        # todo kontrola ci nie sme prilis plny
        self._inventory.append(item)
        return True

    def get_effects(self):
        return self._effects

    def add_effect(self, effect):
        self._effects.append(effect)

    def tick_effects(self):
        for effect in self._effects:
            # effect.tick()
            # todo
            pass

    def is_alive(self):
        return self._health > 0
