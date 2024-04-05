import os.path

from armor import Armor
from effect import Effect
from enums import ArmorType, EffectType
from item import Item

# todo - pridat kontrolu do kazdej set funkcie, ci je to spravneho typu


class Creature:

    class Equipment:
        def __init__(self):
            self._head_armor = None
            self._body_armor = None
            self._legs_armor = None
            self._feet_armor = None
            self._right_hand = None
            self._left_hand = None

        def add_equipment(self, item: Armor):
            if not isinstance(item, Armor):
                return False
            match item.get_armor_type():
                case ArmorType.HEAD:
                    if not item.is_other_better(self._head_armor):
                        self._head_armor = item
                case ArmorType.BODY:
                    if not item.is_other_better(self._body_armor):
                        self._body_armor = item
                case ArmorType.LEGS:
                    if not item.is_other_better(self._legs_armor):
                        self._legs_armor = item
                case ArmorType.FEET:
                    if not item.is_other_better(self._feet_armor):
                        self._feet_armor = item
                case ArmorType.LEFT_ARM:
                    if not item.is_other_better(self._left_hand):
                        self._left_hand = item
                case ArmorType.RIGHT_ARM:
                    if not item.is_other_better(self._right_hand):
                        self._right_hand = item

        def get_equipment(self):
            return [self._head_armor, self._right_hand, self._feet_armor, self._body_armor, self._legs_armor,
                    self._left_hand]

    def __init__(self,
                 health: int = 0,
                 max_health: int = 1,
                 attack: int = 0,
                 defence: int = 0,
                 evasion: int = 0,
                 speed: int = 0,
                 equipment: Equipment = None,
                 inventory: list = None,
                 effects: list = None) -> None:
        self._effects = effects if effects else []
        self._inventory = inventory if inventory else []
        self._equipment = equipment if equipment else self.Equipment()
        self._health = health
        self._max_health = max_health
        self._attack = attack
        self._defence = defence
        self._evasion = evasion
        self._speed = speed
        self._max_inventory = 20  # todo - nech sa to meni podla levelu

    def get_health(self) -> int:
        return self._health

    def set_health(self, new_health: int) -> None:
        self._health = new_health

    def get_max_health(self) -> int:
        return self._max_health

    def set_max_health(self, new_health: int) -> None:
        self._max_health = new_health

    def change_health(self, health_difference: int) -> None:
        self._health += health_difference

    def heal_max(self) -> None:
        self._health = self._max_health

    def get_attack(self) -> int:
        return self._attack

    def set_attack(self, new_attack: int) -> None:
        self._attack = new_attack

    def get_real_attack(self) -> int:
        """
        Computation of real attack - the combination of base attack with each item in equipment and each active effect.
        :return: Number representing the final attack.
        """
        real_attack = self.get_attack()
        for armor in self._equipment.get_equipment():
            if armor:
                real_attack += armor.get_additional_attack()
        # todo + pridat aj z efektov
        return real_attack

    def get_defence(self) -> int:
        return self._defence

    def get_real_defence(self) -> int:
        """
        Computation of real defence - the combination of base defence with each item in equipment and each active
        effect.
        :return:
        """
        real_defence = self.get_defence()
        for armor in self._equipment.get_equipment():
            if armor:
                real_defence += armor.get_additional_defence()
        # todo + pridat aj z efektov
        return real_defence

    def set_defence(self, new_defence: int) -> None:
        self._defence = new_defence

    def get_evasion(self) -> int:
        return self._evasion

    def set_evasion(self, new_evasion: int) -> None:
        self._evasion = new_evasion

    def get_speed(self) -> int:
        return self._speed

    def set_speed(self, new_speed: int) -> None:
        self._speed = new_speed

    def get_equipment(self) -> list:
        return self._equipment.get_equipment()

    def add_item_equipment(self, item: Item) -> bool:
        """
        Function to add item to equipment. If it is not possible to add item to equipment (equipment is full, the item
        was already inside), the function does nothing and returns False. If the item was successfully added then the
        function returns True.
        :param item: Item to be added
        :return: True if item was added, False otherwise
        """
        if not isinstance(item, Armor):
            return False
        return self._equipment.add_equipment(item)

    def get_inventory(self) -> list:
        return self._inventory

    def add_item_inventory(self, item: Item) -> bool:
        """
        Function to add item to equipment. If it is not possible to add item to inventory (inventory is full),
        the function does nothing and returns False. If the item was successfully added then the function returns True.
        :param item: Item to be added
        :return: True if item was added, False otherwise
        """
        if len(self._inventory) > self._max_inventory:
            return False
        self._inventory.append(item)
        return True

    def get_effects(self) -> list:
        return self._effects

    def add_effect(self, effect: Effect) -> None:
        # todo - porozmyslat ci mozeme mat viacnasobne ten isty effekt. Ak nie, pridat na to kontrolu
        self._effects.append(effect)

    def tick_effects(self) -> None:
        to_delete = []
        for effect in self._effects:
            effect_type, change = effect.tick()
            if self._effect_type == EffectType.HEALTH:
                self.change_health(change)
            elif self._effect_type == EffectType.SPEED:
                self.set_speed(self.get_speed() + change)
            elif self._effect_type == EffectType.EVASION:
                self.set_evasion(self.get_evasion() + change)
            if effect.get_effect_duration == 0:
                to_delete.append(effect)
        for effect in to_delete:
            self._effects.remove(effect)

    def is_alive(self) -> bool:
        return self._health > 0

    def get_picture_path(self):
        return os.path.join('graphics', 'error', 'empty.png')
