from enums import PotionType, PotionSize, PotionLevel, EffectType
from item import Item
from effect import Effect


class Potion(Item):
    def __init__(
        self,
        potion_type: PotionType = None,
        potion_size: PotionSize = None,
        potion_level: PotionLevel = PotionLevel.USUAL,
    ):
        self._potion_type = potion_type
        self._potion_size = potion_size
        self._potion_level = potion_level

    def use_potion(self):
        effect = None

        if self._potion_type == PotionType.HEAL:
            effect = Effect(
                EffectType.HEALTH, False, self._potion_level, self._potion_size
            )
        elif self._potion_type == PotionType.HASTE:
            effect = Effect(
                EffectType.SPEED, False, self._potion_level, self._potion_size
            )
        elif self._potion_type == PotionType.SLOW:
            effect = Effect(
                EffectType.SPEED, True, self._potion_level, self._potion_size
            )
        elif self._potion_type == PotionType.POISON:
            effect = Effect(
                EffectType.HEALTH, True, self._potion_level, self._potion_size
            )
        elif self._potion_type == PotionType.EVASION:
            effect = Effect(
                EffectType.EVASION, False, self._potion_level, self._potion_size
            )

        return effect

    def get_potion_type(self):
        return self._potion_type

    def get_potion_size(self):
        return self._potion_size

    def get_potion_level(self):
        return self._potion_level

    def get_potion(self):
        return [self._potion_type, self._potion_size, self._potion_level]
