import random

from enum import Enum


class FieldType(Enum):
    MOUNTAIN = 'mountain'
    PLAINS = 'plains'
    FOREST = 'forest'
    DESERT = 'desert'
    WATER = 'water'


class Field:

    def __init__(self, field_type: FieldType = None, active_objects: list = None, properties: object = None) -> None:
        """
        Initialization of a Field (square on the map)
        :param field_type: Type of the field as an FieldType Object
        :param active_objects: Not implemented yet
        :param properties: Not implemented yet
        """
        if field_type is not None and field_type not in FieldType:
            raise ModuleNotFoundError(f'field type "{field_type}" not found \n Possible types are:{list(FieldType)}')

        self._field_type = field_type if field_type else random.choice(list(FieldType))
        self._properties = properties if properties else {}
        self._active_objects = []
        
        if active_objects is not None:
            self._active_objects.extend(active_objects)

        self._enemy_present = False
        self._player_present = False

    def __eq__(self, other):
        if other is None or not isinstance(other, Field):
            return False
        if self._field_type != other.get_field_type():
            return False
        if self._properties != other.get_properties():
            return False
        if self._active_objects != other.get_active_objects():
            return False
        if self._enemy_present != other.is_enemy_present():
            return False
        if self._player_present != other.is_player_present():
            return False
        return True

    def get_field_type(self) -> FieldType:
        return self._field_type

    def get_properties(self):
        return self._properties

    def get_active_objects(self) -> list:
        return self._active_objects

    def is_player_present(self) -> bool:
        return self._player_present

    def is_enemy_present(self) -> bool:
        return self._enemy_present

    def add_active_object(self, active_object) -> None:  # todo pridat typovanie - co je to zac?
        self._active_objects.append(active_object)

    def remove_object(self, active_object) -> None:  # todo pridat typovanie
        if active_object in self._active_objects:
            self._active_objects.remove(active_object)

    def set_player_present(self, present: bool) -> None:
        self._player_present = present

    def set_enemy_present(self, present: bool) -> None:
        self._enemy_present = present
