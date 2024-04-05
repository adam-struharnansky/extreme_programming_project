from creature import Creature
from enums import EffectType


class Effect:
    def __init__(
        self,
        effect_type: EffectType = None,
        is_negative: bool = False,
        effect_level: int = 1,
        effect_duration: int = 1,
    ):
        self._is_negative = is_negative
        self._effect_level = effect_level
        self._effect_duration = effect_duration
        self._effect_type = effect_type

    def tick(self, creature: Creature):
        self._effect_duration -= 1
        change = self._effect_level * (-1) if self._is_negative else self._effect_level
        if self._effect_type == EffectType.HEALTH:
            creature.change_health(change)
        elif self._effect_type == EffectType.SPEED:
            creature.set_speed(creature.get_speed() + change)
        elif self._effect_type == EffectType.EVASION:
            creature.set_evasion(creature.get_evasion() + change)

    def get_effect_duration(self):
        return self._effect_duration

    def get_effect_level(self):
        return self._effect_level

    def get_effect_type(self):
        return self._effect_type

