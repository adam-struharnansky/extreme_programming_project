import logging
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
    _right_arm_armor: Optional[Armor] = None
    _left_arm_armor: Optional[Armor] = None

    def add_equipment(self, item: Armor) -> bool:
        if not isinstance(item, Armor):
            return False
        logging.debug(f'Adding item to equipment with type: {item.armor_type} and level: {item.armor_level}')
        for armor_type in ArmorType:
            if item.armor_type != armor_type:
                continue
            armor_attr = getattr(self, f"_{armor_type.name.lower()}_armor")
            if not item.is_other_better(armor_attr):
                setattr(self, f"_{armor_type.name.lower()}_armor", item)
                return True
        return False

    def get_equipment(self) -> List[Optional[Armor]]:
        return [self._head_armor, self._right_arm_armor, self._feet_armor, self._body_armor, self._legs_armor,
                self._left_arm_armor]


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

    _alive: bool = True
    _max_inventory: int = 20  # todo: This should change depending on the level
    _picture_path: str = os.path.join('error', 'empty.png')

    def change_health(self, health_difference: int) -> None:
        if not self._alive:
            return
        self.health = min(self.max_health, max(0, self.health + health_difference))
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
        for armor in self.equipment.get_equipment():
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
        for armor in self.equipment.get_equipment():
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
        for effect in self.effects:
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

    def get_equipment(self) -> list[Optional[Armor]]:
        return self.equipment.get_equipment()

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
        return self.equipment.add_equipment(item)

    def add_item_to_inventory(self, item: Item) -> bool:
        """
        Function to add item to equipment. If it is not possible to add item to inventory (inventory is full),
        the function does nothing and returns False. If the item was successfully added then the function returns True
        :param item: Item to be added
        :return: True if item was added, False otherwise
        """
        if not self._alive:
            return False
        if len(self.inventory) > self._max_inventory:
            return False
        self.inventory.append(item)
        return True

    def add_effect(self, effect: Effect) -> None:
        # if there is the same type of effect only the duration is changed (not adding new one)
        if not self._alive:
            return
        if effect in self.effects:
            self.effects[self.effects.index(effect)].effect_duration = effect.effect_duration
        elif effect:
            self.effects.append(effect)

    def tick_effects(self) -> None:
        to_delete = []
        for effect in self.effects:
            effect_type, change = effect.tick()
            if effect_type == EffectType.HEALTH:
                self.change_health(change)
            if effect.effect_duration == 0:
                to_delete.append(effect)

        for effect in to_delete:
            self.effects.remove(effect)

    def use_random_potion(self):
        if self.inventory:  # todo: Can't be there other items in the inventory?
            rnd = random.randint(0, len(self.inventory) - 1)
            self.add_effect(self.inventory[rnd].use_potion())
            self.inventory.remove(self.inventory[rnd])

    def is_alive(self) -> bool:
        return self._alive

    @property
    def picture_path(self) -> str:
        return self._picture_path
