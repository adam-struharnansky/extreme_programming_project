import pytest

from source.game.characters import Creature
from source.game.items import Armor, generate_random_armor
from source.auxiliary import ArmorType, ItemLevel


def test_health():
    creature = Creature(10, 100)
    assert creature.health == 10
    assert creature.max_health == 100
    assert creature.is_alive()
    # testing the increasing of health
    health = 10
    for i in range(10):
        creature.change_health(i)
        health += i
        assert creature.health == health
        assert creature.is_alive()
    # testing the max health
    creature.heal_to_max()
    assert creature.health == 100
    assert creature.is_alive()
    # testing that the max health cannot be crossed
    for i in range(10):
        creature.change_health(i + 1)
        assert creature.health == 100
        assert creature.is_alive()
    creature.change_health(-10)
    assert creature.health == 90
    creature.change_health(20)
    assert creature.health == 100
    # testing decreasing of health
    for i in range(99):
        creature.change_health(-1)
        assert creature.health == 99 - i
        assert creature.is_alive()
    # testing the death by decreasing the health to 0
    creature.change_health(-1)
    assert creature.health == 0
    assert not creature.is_alive()
    # testing the fact that dead cannot be revived by simply adding health
    for i in range(10):
        creature.change_health(i)
        assert creature.health == 0
        assert not creature.is_alive()
    assert creature.max_health == 100
    creature.heal_to_max()
    assert creature.health == 0
    assert not creature.is_alive()


def test_equipment():
    creature = Creature()
    assert all(a is None for a in creature.get_equipment())
    # testing head armor
    armor_hb = Armor(armor_type=ArmorType.HEAD, armor_level=ItemLevel.BRONZE)
    creature.add_item_to_equipment(armor_hb)
    assert armor_hb == creature.get_equipment()[0]
    assert all(a is None for a in creature.get_equipment()[1:])
    armor_hs = Armor(armor_type=ArmorType.HEAD, armor_level=ItemLevel.SILVER)
    creature.add_item_to_equipment(armor_hs)
    assert armor_hs == creature.get_equipment()[0]
    assert all(a is None for a in creature.get_equipment()[1:])
    # testing shield armor / left hand armor
    armor_ls = Armor(armor_type=ArmorType.LEFT_ARM, armor_level=ItemLevel.SILVER)
    creature.add_item_to_equipment(armor_ls)
    assert armor_ls == creature.get_equipment()[5]
    assert all(a is None for a in creature.get_equipment()[1:5])
    armor_lg = Armor(armor_type=ArmorType.LEFT_ARM, armor_level=ItemLevel.GOLD)
    creature.add_item_to_equipment(armor_lg)
    assert creature.get_equipment()[5] == armor_lg
    assert all(a is None for a in creature.get_equipment()[1:5])
    armor_ll = Armor(armor_type=ArmorType.LEFT_ARM, armor_level=ItemLevel.LEGENDARY)
    creature.add_item_to_equipment(armor_ll)
    assert creature.get_equipment()[5] == armor_ll
    assert all(a is None for a in creature.get_equipment()[1:5])


def test_real_attack():
    creature = Creature(attack=10)
    assert creature.attack == 10
    assert creature.get_real_attack() == 10

    sword_bronze = None
    while not sword_bronze:
        possible_sword = generate_random_armor(ItemLevel.BRONZE)
        if possible_sword.armor_type == ArmorType.RIGHT_ARM:
            sword_bronze = possible_sword
    creature.add_item_to_equipment(sword_bronze)
    assert creature.get_real_attack() > 10

    previous_real_attack = creature.get_real_attack()
    sword_silver = None
    while not sword_silver:
        possible_sword = generate_random_armor(ItemLevel.SILVER)
        if possible_sword.armor_type == ArmorType.RIGHT_ARM:
            sword_silver = possible_sword
    creature.add_item_to_equipment(sword_silver)
    assert creature.get_real_attack() > previous_real_attack

    previous_real_attack = creature.get_real_attack()
    sword_gold = None
    while not sword_gold:
        possible_sword = generate_random_armor(ItemLevel.GOLD)
        if possible_sword.armor_type == ArmorType.RIGHT_ARM:
            sword_gold = possible_sword
    creature.add_item_to_equipment(sword_gold)
    assert creature.get_real_attack() > previous_real_attack

    previous_real_attack = creature.get_real_attack()
    sword_legendary = None
    while not sword_legendary:
        possible_sword = generate_random_armor(ItemLevel.LEGENDARY)
        if possible_sword.armor_type == ArmorType.RIGHT_ARM:
            sword_legendary = possible_sword
    creature.add_item_to_equipment(sword_legendary)
    assert creature.get_real_attack() > previous_real_attack

    # todo: Add test for change the real attack when using potions/under effects


def test_real_defence():
    creature = Creature(defence=10)
    assert creature.defence == 10
    assert creature.get_real_defence() == 10

    shield_bronze = None
    while not shield_bronze:
        possible_shield = generate_random_armor(ItemLevel.BRONZE)
        if possible_shield.armor_type == ArmorType.LEFT_ARM:
            shield_bronze = possible_shield
    creature.add_item_to_equipment(shield_bronze)
    assert creature.get_real_defence() > 10

    previous_real_defence = creature.get_real_defence()
    shield_silver = None
    while not shield_silver:
        possible_shield = generate_random_armor(ItemLevel.SILVER)
        if possible_shield.armor_type == ArmorType.LEFT_ARM:
            shield_silver = possible_shield
    creature.add_item_to_equipment(shield_silver)
    assert creature.get_real_defence() > previous_real_defence

    previous_real_defence = creature.get_real_defence()
    shield_gold = None
    while not shield_gold:
        possible_shield = generate_random_armor(ItemLevel.GOLD)
        if possible_shield.armor_type == ArmorType.LEFT_ARM:
            shield_gold = possible_shield
    creature.add_item_to_equipment(shield_gold)
    assert creature.get_real_defence() > previous_real_defence

    previous_real_defence = creature.get_real_defence()
    shield_legendary = None
    while not shield_legendary:
        possible_shield = generate_random_armor(ItemLevel.LEGENDARY)
        if possible_shield.armor_type == ArmorType.LEFT_ARM:
            shield_legendary = possible_shield
    creature.add_item_to_equipment(shield_legendary)
    assert creature.get_real_defence() > previous_real_defence

    # todo: Add test for change the real defence when using potions/under effects


@pytest.mark.skip(reason="Test not implemented yet")
def test_potions():
    # todo
    assert False, "Test not implemented yet"


@pytest.mark.skip(reason="Test not implemented yet")
def test_effects():
    # todo
    assert False, "Test not implemented yet"
