import pytest
from field import *

def test_field_eq():
    field_1 = Field("forest")
    field_2 = Field("forest")

    assert field_1 == field_2

    field_1.field_type = "mountain"
    assert field_1 != field_2
    field_1.field_type = "forest"

    assert field_1 == field_2

    field_1.properties[5] = 5
    assert field_1 != field_2
    field_1.properties = {}

    assert field_1 == field_2

    field_1.objects = [5]
    assert field_1 != field_2
    field_1.objects = []

    field_1.enemy_present = True
    assert field_1 != field_2
    field_1.enemy_present = False
