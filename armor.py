import random

from enums import ArmorType, ItemLevel
from item import Item


class Armor(Item):
    def __init__(self, armor_type: ArmorType = None, armor_level: ItemLevel = None, additional_attack: int = 0,
                 additional_defence: int = 0, picture_path: str = None):
        super().__init__()

        self._armor_type = armor_type if armor_type else random.choice(list(ArmorType))
        self._armor_level = armor_level if armor_level else random.choice(list(ItemLevel))
        self._additional_attack = additional_attack
        self._additional_defence = additional_defence
        self._picture_path = picture_path if picture_path else None  # todo - prazdny obrazok

    def get_armor_type(self) -> ArmorType:  # todo - pochopit ako toto funguje
        return self._armor_type

    def get_armor_level(self) -> ItemLevel:
        return self._armor_level

    def get_additional_defence(self):
        return self._additional_defence

    def get_additional_attack(self):
        return self._additional_attack

    def is_better(self, other):
        if other is None:
            return False
        return (self.get_additional_attack() + self.get_additional_defence()) < \
               (other.get_additional_attack() + other.get_additional_defence())

    def get_picture_path(self):
        return self._picture_path
