import os.path
import random

from dataclasses import dataclass, field
from typing import List, Optional

from source.auxiliary import ArmorType, EffectType
from source.game.items import Armor
from source.game.items import Effect
from source.game.items import Item


@dataclass
class _Equipment:
    _head_armor: Optional[Armor] = None
    _body_armor: Optional[Armor] = None
    _legs_armor: Optional[Armor] = None
    _feet_armor: Optional[Armor] = None
    _right_hand: Optional[Armor] = None
    _left_hand: Optional[Armor] = None

    def add_equipment(self, item: Armor) -> bool:
        if not isinstance(item, Armor):
            return False
        match item.armor_type:
            case ArmorType.HEAD:
                if not item.is_other_better(self._head_armor):
                    self._head_armor = item
                    return True
            case ArmorType.BODY:
                if not item.is_other_better(self._body_armor):
                    self._body_armor = item
                    return True
            case ArmorType.LEGS:
                if not item.is_other_better(self._legs_armor):
                    self._legs_armor = item
                    return True
            case ArmorType.FEET:
                if not item.is_other_better(self._feet_armor):
                    self._feet_armor = item
                    return True
            case ArmorType.LEFT_ARM:
                if not item.is_other_better(self._left_hand):
                    self._left_hand = item
                    return True
            case ArmorType.RIGHT_ARM:
                if not item.is_other_better(self._right_hand):
                    self._right_hand = item
                    return True
        return False

    def get_equipment(self) -> List[Optional[Armor]]:
        return [self._head_armor, self._right_hand, self._feet_armor, self._body_armor, self._legs_armor,
                self._left_hand]


@dataclass
class Creature:
    health: int = 0
    max_health: int = 1
    attack: int = 0
    defence: int = 0
    evasion: int = 0
    speed: int = 0
    equipment: _Equipment = field(default_factory=_Equipment)
    inventory: List[Item] = field(default_factory=list)
    effects: List[Effect] = field(default_factory=list)

    _alive = True
    _max_inventory: int = 20  # todo: This should change depending on the level
    _picture_path: str = os.path.join('error', 'empty.png')

    def __post_init__(self):
        self._effects = self.effects if self.effects else []
        self._inventory = self.inventory if self.inventory else []
        self._equipment = self.equipment if self.equipment else _Equipment()

    def change_health(self, health_difference: int) -> None:
        if not self._alive:
            return
        self.health += min(self.max_health, max(0, health_difference))
        if self.health == 0:
            self._alive = False

    def heal_to_max(self) -> None:
        if not self._alive:
            return
        self.health = self.max_health

    def get_real_attack(self) -> int:
        """
        Computation of real attack - the combination of base attack with each item in equipment and each active effect.
        :return: Number representing the final attack.
        """
        if not self._alive:
            return 0
        real_attack = self.attack
        for armor in self._equipment.get_equipment():
            if armor:
                real_attack += armor.additional_attack
        # todo: Add change also from the effects
        return real_attack

    def get_real_defence(self) -> int:
        """
        Computation of real defence - the combination of base defence with each item in equipment and each active
        effect.
        :return:
        """
        if not self._alive:
            return 0
        real_defence = self.defence
        for armor in self._equipment.get_equipment():
            if armor:
                real_defence += armor.additional_defence
        # todo: Add change also from the effects
        return real_defence

    def get_real_evasion(self) -> int:
        """
        Computation of real evasion - the combination of base evasion with each item in equipment and each active
        effect.
        :return:
        """
        if not self._alive:
            return 0
        real_evasion = self.evasion
        for effect in self._effects:
            if effect.effect_type == EffectType.EVASION:
                real_evasion += effect.get_change()
        return real_evasion

    def get_real_speed(self) -> int:
        """
        Computation of real speed - the combination of base speed with each item in equipment and each active
        effect.
        :return:
        """
        if not self._alive:
            return 0
        real_speed = self.speed
        for effect in self.effects:
            if effect.effect_type == EffectType.SPEED:
                real_speed += effect.get_change()
        return real_speed

    def get_equipment(self) -> list:
        return self._equipment.get_equipment()

    def add_item_to_equipment(self, item: Item) -> bool:
        """
        Function to add item to equipment. If it is not possible to add item to equipment (equipment is full, the item
        was already inside), the function does nothing and returns False. If the item was successfully added then the
        function returns True
        :param item: Item to be added
        :return: True if item was added, False otherwise
        """
        if not self._alive:
            return False
        if not isinstance(item, Armor):
            return False
        return self._equipment.add_equipment(item)

    def add_item_to_inventory(self, item: Item) -> bool:
        """
        Function to add item to equipment. If it is not possible to add item to inventory (inventory is full),
        the function does nothing and returns False. If the item was successfully added then the function returns True
        :param item: Item to be added
        :return: True if item was added, False otherwise
        """
        if not self._alive:
            return False
        if len(self._inventory) > self._max_inventory:
            return False
        self._inventory.append(item)
        return True

    def add_effect(self, effect: Effect) -> None:
        # if there is the same type of effect only the duration is changed (not adding new one)
        if not self._alive:
            return
        if effect in self._effects:
            self._effects[self._effects.index(effect)].effect_duration = effect.effect_duration
        elif effect:
            self._effects.append(effect)

    def tick_effects(self) -> None:
        to_delete = []
        for effect in self._effects:
            effect_type, change = effect.tick()
            if effect_type == EffectType.HEALTH:
                self.change_health(change)
            if effect.effect_duration == 0:
                to_delete.append(effect)

        for effect in to_delete:
            self._effects.remove(effect)

    def use_random_potion(self):
        if self._inventory:  # todo: Can't be there other items in the inventory?
            rnd = random.randint(0, len(self._inventory) - 1)
            self.add_effect(self._inventory[rnd].use_potion())
            self._inventory.remove(self._inventory[rnd])

    def is_alive(self) -> bool:
        return self._alive

    @property
    def picture_path(self) -> str:
        return self._picture_path
