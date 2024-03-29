
class Creature:
    def __init__(self):
        self._health = 0
        self._attack = 0
        self._defence = 0
        self._evasion = 0
        self._equipment = []
        self._inventory = []
        self._effects = []

    def get_health(self) -> int:
        return self._health

    def set_health(self, new_health:int) -> None:
        self._health = new_health

    def change_health(self, health_difference:int) -> None:
        self._health += health_difference

    def get_attack(self) -> int:
        return self._attack

    def set_attack(self, new_attack:int) -> None:
        self._attack = new_attack

    def get_real_attack(self) -> int:
        # todo + pridat aj z equipmentu
        return self.get_attack()

    def get_defence(self) -> int:
        return self._defence

    def set_defence(self, new_defence:int) -> None:
        self._defence = new_defence

    def get_evasion(self) -> int:
        return self._evasion

    def set_evasion(self, new_evasion:int) -> None:
        self._evasion = new_evasion

    def get_equipment(self) -> list:
        return self._equipment

    def add_item_equipment(self, item) -> bool: #todo pridat typ pre item
        # todo kontrola - nechceme mat naraz dva mece, atd
        self._equipment.append(item)
        return True # podla toho, ci sa podarilo vlzoit, alebo nie

    def get_inventory(self) -> list:
        return self._inventory

    def add_item_inventory(self, item) -> bool: #todo pridat typ pre item
        # todo kontrola ci nie sme prilis plny
        self._inventory.append(item)
        return True

    def get_effects(self) -> list:
        return self._effects

    def add_effect(self, effect) -> None: #todo pridat typ pre effect
        self._effects.append(effect)

    def tick_effects(self) -> None:
        for effect in self._effects:
            # effect.tick()
            # todo
            pass
