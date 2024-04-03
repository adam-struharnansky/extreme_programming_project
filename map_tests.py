import pytest
from map import *


def test_item_duplicity():
    mp = Map(None, None)
    mp.generate_map()
    mp.save_map("data/test.pickle")
    new_mp = Map(None, None)
    new_mp.load_map("data/test.pickle")

    assert mp.dat.map == new_mp.dat.map
    assert mp.dat.field_size == new_mp.dat.field_size
    assert mp.dat.player_pos == new_mp.dat.player_pos
    assert mp.dat.player == new_mp.dat.player
