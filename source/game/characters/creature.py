import os.path
import random

from source.auxiliary.enums import ArmorType, EffectType
from source.game.items.armor import Armor
from source.game.items.effect import Effect
from source.game.items.item import Item

# todo: Pridat kontrolu do kazdej set funkcie, ci je to spravneho typu


class Creature:

    class _Equipment:
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
                 equipment: _Equipment = None,
                 inventory: list = None,
                 effects: list = None) -> None:
        self._effects = effects if effects else []
        self._inventory = inventory if inventory else []
        self._equipment = equipment if equipment else self._Equipment()
        self._health = health
        self._max_health = max_health
        self._attack = attack
        self._defence = defence
        self._evasion = evasion
        self._speed = speed
        self._max_inventory = 20  # todo: Nech sa to meni podla levelu
        self._picture_path = os.path.join('error', 'empty.png')

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, new_health: int) -> None:
        self._health = new_health

    def change_health(self, health_difference: int) -> None:
        self._health += health_difference

    def heal_to_max(self) -> None:
        self._health = self._max_health

    @property
    def max_health(self) -> int:
        return self._max_health

    @max_health.setter
    def max_health(self, new_health: int) -> None:
        self._max_health = new_health

    @property
    def attack(self) -> int:
        return self._attack

    @attack.setter
    def attack(self, new_attack: int) -> None:
        self._attack = new_attack

    def get_real_attack(self) -> int:
        """
        Computation of real attack - the combination of base attack with each item in equipment and each active effect.
        :return: Number representing the final attack.
        """
        real_attack = self.attack
        for armor in self._equipment.get_equipment():
            if armor:
                real_attack += armor.additional_attack
        # todo: Pridat zmenu aj z efektov
        return real_attack

    @property
    def defence(self) -> int:
        return self._defence

    @defence.setter
    def defence(self, new_defence: int) -> None:
        self._defence = new_defence

    def get_real_defence(self) -> int:
        """
        Computation of real defence - the combination of base defence with each item in equipment and each active
        effect.
        :return:
        """
        real_defence = self.defence
        for armor in self._equipment.get_equipment():
            if armor:
                real_defence += armor.additional_defence
        # todo: Pridat zmenu aj z efektov
        return real_defence

    @property
    def evasion(self) -> int:
        return self._evasion

    @evasion.setter
    def evasion(self, new_evasion: int) -> None:
        self._evasion = new_evasion

    def get_real_evasion(self) -> int:
        """
        Computation of real evasion - the combination of base evasion with each item in equipment and each active
        effect.
        :return:
        """
        real_evasion = self.evasion
        for effect in self._effects:
            if effect.effect_type == EffectType.EVASION:
                real_evasion += effect.get_change()
        return real_evasion

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, new_speed: int) -> None:
        self._speed = new_speed
    
    def get_real_speed(self) -> int:
        """
        Computation of real speed - the combination of base speed with each item in equipment and each active
        effect.
        :return:
        """
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
        if not isinstance(item, Armor):
            return False
        return self._equipment.add_equipment(item)

    @property
    def inventory(self) -> list:
        return self._inventory

    def add_item_to_inventory(self, item: Item) -> bool:
        """
        Function to add item to equipment. If it is not possible to add item to inventory (inventory is full),
        the function does nothing and returns False. If the item was successfully added then the function returns True
        :param item: Item to be added
        :return: True if item was added, False otherwise
        """
        if len(self._inventory) > self._max_inventory:
            return False
        self._inventory.append(item)
        return True

    @property
    def effects(self) -> list:
        return self._effects

    def add_effect(self, effect: Effect) -> None:
        # ak existuje taky isty effect aktualizuje jeho duration
        if effect in self._effects:
            self._effects[self._effects.index(effect)].effect_duration=effect.effect_duration
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
        if(self._inventory):
            rnd = random.randint(0, len(self._inventory)-1)
            self.add_effect(self._inventory[rnd].use_potion())
            self._inventory.remove(self._inventory[rnd])

    def is_alive(self) -> bool:
        return self._health > 0

    @property
    def picture_path(self) -> str:
        return self._picture_path
