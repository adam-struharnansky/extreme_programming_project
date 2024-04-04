import pytest
from field import *


def test_field_eq():
    field_1 = Field(FieldType.FOREST)
    field_2 = Field(FieldType.FOREST)

    assert field_1 == field_2

    field_1._field_type = FieldType.MOUNTAIN
    assert field_1 != field_2
    field_1._field_type = FieldType.FOREST

    assert field_1 == field_2

    field_1._properties[5] = 5
    assert field_1 != field_2
    field_1._properties = {}

    assert field_1 == field_2

    field_1._active_objects = [5]
    assert field_1 != field_2
    field_1._active_objects = []

    field_1._enemy_present = True
    assert field_1 != field_2
    field_1._enemy_present = False
