import pytest
from map import *


def test_item_duplicity():

    mp = Map(None, None)
    mp.generate_map()
    mp.save_map("data/test.pickle")
    new_mp = Map(None, None)
    new_mp.load_map("data/test.pickle")

    assert mp._dat.map == new_mp._dat.map
    assert mp._dat.field_size == new_mp._dat.field_size
    assert mp._dat.player_pos == new_mp._dat.player_pos
    assert mp._dat.player == new_mp._dat.player


def test_move_right():
    map_obj = Map(None, None)
    map_obj.generate_map()

    initial_pos = map_obj._dat.player_pos.copy()
    map_obj.move(1073741903)  # The key code for the right arrow key
    assert map_obj._dat.player_pos[0] == initial_pos[0] + 1
    assert map_obj._dat.player_pos[1] == initial_pos[1]


def test_move_left():
    map_obj = Map(None, None)
    map_obj.generate_map()

    initial_pos = map_obj._dat.player_pos.copy()
    map_obj.move(1073741904)  # The key code for the left arrow key

    assert map_obj._dat.player_pos[0] == initial_pos[0] - 1
    assert map_obj._dat.player_pos[1] == initial_pos[1]


def test_move_up():
    map_obj = Map(None, None)
    map_obj.generate_map()

    initial_pos = map_obj._dat.player_pos.copy()
    map_obj.move(1073741906)  # The key code for the up arrow key

    assert map_obj._dat.player_pos[0] == initial_pos[0]
    assert map_obj._dat.player_pos[1] == initial_pos[1] - 1


def test_move_down():
    map_obj = Map(None, None)
    map_obj.generate_map()

    initial_pos = map_obj._dat.player_pos.copy()
    map_obj.move(1073741905)  # The key code for the down arrow key

    assert map_obj._dat.player_pos[0] == initial_pos[0]
    assert map_obj._dat.player_pos[1] == initial_pos[1] + 1

def test_move_down():
    map_obj = Map(None, None)
    map_obj.generate_map()

    initial_pos = map_obj._dat.player_pos.copy()
    map_obj.move(1073741905)  # The key code for the down arrow key

    assert map_obj._dat.player_pos[0] == initial_pos[0]
    assert map_obj._dat.player_pos[1] == initial_pos[1] + 1
