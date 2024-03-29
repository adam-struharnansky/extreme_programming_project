
class Creature:
    def __init__(self,
                 health:int=0,
                 attack:int=0,
                 defence:int=0,
                 evasion:int=0,
                 equipment:list=None,
                 inventory:list=None,
                 effects:list=None) -> None:

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
        return True  # podla toho, ci sa podarilo vlzoit, alebo nie

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

    def is_alive(self) -> bool:
        return self._health > 0
