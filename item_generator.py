
import os
import random

from enums import ItemLevel, ArmorType
from item import Item
from armor import Armor


def generate_random_item(item_level: ItemLevel = None) -> Item:
    item_level = item_level if item_level else ItemLevel.BRONZE

    # todo - dalsie typy itemov, ak vobec sa do tohoto pustime
    item_types_number = [1]
    generated_item_type = random.choice(item_types_number)

    match generated_item_type:
        case 1:
            return generate_random_armor(item_level)


def generate_random_armor(item_level: ItemLevel = None) -> Armor:
    # todo - vytvorit vsetky itemy ako pickle files, a potom iba z toho nahodne vyberat
    item_level = item_level if item_level else ItemLevel.BRONZE
    armor_type = random.choices(list(ArmorType))

    additional_defence = 0
    additional_attack = 0
    file_name = ''
    match armor_type[0]:
        case ArmorType.HEAD:
            additional_defence = 8
            additional_attack = 1
            file_name = 'head_armor'
        case ArmorType.BODY:
            additional_defence = 10
            additional_attack = 1
            file_name = 'body_armor'
        case ArmorType.LEGS:
            additional_defence = 6
            additional_attack = 1
            file_name = 'legs_armor'
        case ArmorType.LEFT_ARM:
            additional_defence = 10
            additional_attack = 3
            file_name = 'left_armor'
        case ArmorType.RIGHT_ARM:
            additional_defence = 1
            additional_attack = 10
            file_name = 'right_armor'
        case ArmorType.FEET:
            additional_defence = 3
            additional_attack = 2
            file_name = 'feet_armor'

    match item_level:
        case ItemLevel.BRONZE:
            additional_defence *= 1
            additional_attack *= 1
            file_name = file_name + '_bronze.png'
        case ItemLevel.SILVER:
            additional_defence *= 2
            additional_attack *= 2
            file_name = file_name + '_silver.png'
        case ItemLevel.GOLD:
            additional_defence *= 3
            additional_attack *= 3
            file_name = file_name + '_gold.png'
        case ItemLevel.LEGENDARY:
            additional_defence *= 4
            additional_attack *= 4
            file_name = file_name + '_legendary.png'

    path = 'graphics/' + file_name
    # todo - pouzit os
    return Armor(armor_type, item_level, additional_attack, additional_defence, path)