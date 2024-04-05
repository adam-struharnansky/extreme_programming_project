
from player import *


def test_player_eq():
    player_1 = Player()
    player_2 = Player()

    assert player_1 == player_2

    player_1._health = 100
    assert player_1._health != player_2._health
    player_1._health = 0

    assert player_1 == player_2

    player_1._max_health = 100
    assert player_1._max_health != player_2._max_health
    player_1._max_health = 1

    assert player_1 == player_2

    player_1._attack = 100
    assert player_1._attack != player_2._attack
    player_1._attack = 0

    assert player_1 == player_2

    player_1._defence = 100
    assert player_1._defence != player_2._defence
    player_1._defence = 0

    assert player_1 == player_2

    player_1._evasion = 100
    assert player_1._evasion != player_2._evasion
    player_1._evasion = 0

    assert player_1 == player_2

    player_1._speed = 100
    assert player_1._speed != player_2._speed
    player_1._speed = 0

    assert player_1 == player_2

    player_1._equipment = [100]
    assert player_1._equipment != player_2._equipment
    player_1._equipment = []

    assert player_1 == player_2

    player_1._inventory = [100]
    assert player_1._inventory != player_2._inventory
    player_1._inventory = []

    assert player_1 == player_2

    player_1._effects = [100]
    assert player_1._effects != player_2._effects
    player_1._effects = []

    assert player_1 == player_2

    player_1._name = "name"
    assert player_1._name != player_2._name
    player_1._name = ""

    assert player_1 == player_2

    player_1._level = 100
    assert player_1._level != player_2._level
    player_1._level = 0

    assert player_1 == player_2

    player_1._current_experience = 100
    assert player_1._current_experience != player_2._current_experience
    player_1._current_experience = 0

    assert player_1 == player_2

    player_1._next_level_experience = 100
    assert player_1._next_level_experience != player_2._next_level_experience
    player_1._next_level_experience = 2

    assert player_1 == player_2
