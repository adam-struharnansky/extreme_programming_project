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
