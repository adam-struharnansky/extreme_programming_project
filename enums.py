from enum import Enum, IntEnum, auto


class Key(Enum):
    UP = 1073741906
    DOWN = 1073741905
    LEFT = 1073741904
    RIGHT = 1073741903


class ArmorType(Enum):
    HEAD = auto()
    BODY = auto()
    LEGS = auto()
    LEFT_ARM = auto()
    RIGHT_ARM = auto()
    FEET = auto()


class ItemLevel(Enum):
    BRONZE = 0
    SILVER = 1
    GOLD = 2
    LEGENDARY = 3


class EffectType(Enum):
    HEALTH = auto()
    SPEED = auto()
    EVASION = auto()
    IMMORTALITY = auto()


class PotionType(Enum):
    HEAL = "heal"
    HASTE = "haste"
    POISON = "poison"
    SLOW = "slow"
    EVASION = "evasion"


class PotionSize(Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3


class PotionLevel(Enum):
    USUAL = 1
    RARE = 2
    LEGENDARY = 3


class FieldType(Enum):
    MOUNTAIN = 'mountain'
    PLAINS = 'plains'
    FOREST = 'forest'
    DESERT = 'desert'
    WATER = 'water'
