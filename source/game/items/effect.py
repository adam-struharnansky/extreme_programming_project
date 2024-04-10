from auxiliary.enums import EffectType


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

    def __eq__(self, other) -> bool:
        if self._effect_type != other.effect_type:
            return False
        elif self.get_change() != other.get_change():
            return False
        return True
    
    def tick(self):
        self._effect_duration -= 1
        return self._effect_type, self.get_change()

    @property
    def effect_duration(self):
        return self._effect_duration
    
    @effect_duration.setter
    def effect_duration(self, new_duration: int) -> None:
        self._effect_duration = new_duration
    
    @property
    def effect_level(self):
        return self._effect_level
    
    @property
    def effect_type(self):
        return self._effect_type
    
    def get_change(self):
        return self._effect_level * (-1) if self._is_negative else self._effect_level
