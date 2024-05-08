
import os
import random

from source.auxiliary import ArmorType, ItemLevel
from source.game.items import Item


class Armor(Item):
    def __init__(self, armor_type: ArmorType = None, armor_level: ItemLevel = None, additional_attack: int = 0,
                 additional_defence: int = 0, picture_path: str = None):
        super().__init__()
        self._armor_type = armor_type or random.choice(list(ArmorType))
        self._armor_level = armor_level or random.choice(list(ItemLevel))
        self._additional_attack = additional_attack
        self._additional_defence = additional_defence
        self._picture_path = picture_path or os.path.join('error', 'empty.png')

    @property
    def armor_type(self) -> ArmorType:
        return self._armor_type

    @property
    def armor_level(self) -> ItemLevel:
        return self._armor_level

    @property
    def additional_defence(self) -> int:
        return self._additional_defence

    @property
    def additional_attack(self) -> int:
        return self._additional_attack

    def is_other_better(self, other: 'Armor' = None) -> bool:
        if other is None:
            return False
        if not isinstance(other, Armor):
            return False
        return (self.additional_attack + self.additional_defence) < \
               (other.additional_attack + other.additional_defence)

    @property
    def picture_path(self) -> str:
        return self._picture_path
