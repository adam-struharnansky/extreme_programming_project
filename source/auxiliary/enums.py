"""
enums

This module contains all enums used in program in one place.

"""


from enum import auto, Enum

# try to keep enums in this file alphabetical
# try to use auto(), if the values of enums are not important


class ArmorType(Enum):
    HEAD = auto()
    BODY = auto()
    LEGS = auto()
    LEFT_ARM = auto()
    RIGHT_ARM = auto()
    FEET = auto()


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class EffectType(Enum):
    HEALTH = "health"
    SPEED = "speed"
    EVASION = "evasion"
    IMMORTALITY = "immortality"


class FieldType(Enum):
    MOUNTAIN = auto()
    PLAINS = auto()
    FOREST = auto()
    DESERT = auto()
    WATER = auto()


class GameState(Enum):
    MENU = auto()
    LOADING_NEW_GAME = auto()
    LOADING_EXISTING_GAME = auto()
    PLAYING_GAME = auto()
    LOST_GAME = auto()


class ItemLevel(Enum):
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()
    LEGENDARY = auto()


class KeyStates(Enum):
    UNPRESSED = auto()
    PRESSED = auto()
    PROCESSED = auto()


class MapSize(Enum):
    SMALL = (50, 50)
    MEDIUM = (80, 80)
    LARGE = (120, 120)


class MapType(Enum):
    RANDOM = 'Random'
    SMALL_BIOMES = 'Small Biomes'
    LARGE_BIOMES = 'Large Biomes'


class PotionLevel(Enum):
    USUAL = 1
    RARE = 2
    LEGENDARY = 3


class PotionSize(Enum):
    SMALL = 3
    MEDIUM = 5
    BIG = 7


class PotionType(Enum):
    HEAL = "heal"
    HASTE = "haste"
    POISON = "poison"
    SLOW = "slow"
    EVASION = "evasion"
