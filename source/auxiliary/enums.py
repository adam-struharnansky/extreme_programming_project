from enum import auto, Enum


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
    HEALTH = "health"
    SPEED = "speed"
    EVASION = "evasion"
    IMMORTALITY = "immortality"


class PotionType(Enum):
    HEAL = "heal"
    HASTE = "haste"
    POISON = "poison"
    SLOW = "slow"
    EVASION = "evasion"


class PotionSize(Enum):
    SMALL = 3
    MEDIUM = 5
    BIG = 7


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


class GameState(Enum):
    MENU = 0
    LOADING_NEW_GAME = 1
    LOADING_EXISTING_GAME = 2
    PLAYING_GAME = 3
    LOST_GAME = 4
