import random
from effect import Effect
from auxiliary.enums import EffectType, PotionLevel, PotionSize, PotionType
from item import Item


class Potion(Item):
    def __init__(self, potion_type: PotionType = None, potion_size: PotionSize = None,
                 potion_level: PotionLevel = None):
        super().__init__()
        self._potion_type = potion_type if potion_type else random.choice(list(PotionType))
        self._potion_size = potion_size if potion_size else random.choice(list(PotionSize))
        self._potion_level = potion_level if potion_level else random.choice(list(PotionLevel))

    def use_potion(self):
        effect = None

        if self._potion_type == PotionType.HEAL:
            effect = Effect(
                EffectType.HEALTH, False, self._potion_level.value, self._potion_size.value
            )
        elif self._potion_type == PotionType.HASTE:
            effect = Effect(
                EffectType.SPEED, False, self._potion_level.value, self._potion_size.value
            )
        elif self._potion_type == PotionType.SLOW:
            effect = Effect(
                EffectType.SPEED, True, self._potion_level.value, self._potion_size.value
            )
        elif self._potion_type == PotionType.POISON:
            effect = Effect(
                EffectType.HEALTH, True, self._potion_level.value, self._potion_size.value
            )
        elif self._potion_type == PotionType.EVASION:
            effect = Effect(
                EffectType.EVASION, False, self._potion_level.value, self._potion_size.value
            )

        return effect

    @property
    def potion_type(self):
        return self._potion_type

    @property
    def potion_size(self):
        return self._potion_size

    @property
    def potion_level(self):
        return self._potion_level

    def get_potion(self):
        return [self._potion_type, self._potion_size, self._potion_level]
