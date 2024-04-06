import os.path
import random

from auxiliary.enums import FieldType


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
        self._picture_path = os.path.join('graphics', 'error', 'empty.png')
        match self._field_type:
            case FieldType.WATER:
                self._picture_path = os.path.join('graphics', 'map_tiles', 'water.png')
            case FieldType.FOREST:
                self._picture_path = os.path.join('graphics', 'map_tiles', 'forest.png')
            case FieldType.MOUNTAIN:
                self._picture_path = os.path.join('graphics', 'map_tiles', 'mountain.png')
            case FieldType.PLAINS:
                self._picture_path = os.path.join('graphics', 'map_tiles', 'plains.png')
            case FieldType.DESERT:
                self._picture_path = os.path.join('graphics', 'map_tiles', 'desert.png')

    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, Field):
            return False
        if self._field_type != other.field_type:
            return False
        if self._properties != other.properties:
            return False
        if self._active_objects != other.active_objects:
            return False
        if self._enemy_present != other.enemy_present:
            return False
        return True

    @property
    def field_type(self) -> FieldType:
        return self._field_type

    @property
    def properties(self):
        return self._properties

    @property
    def active_objects(self) -> list:
        return self._active_objects

    @property
    def enemy_present(self) -> bool:
        return self._enemy_present

    @enemy_present.setter
    def enemy_present(self, present: bool) -> None:
        self._enemy_present = present

    def add_active_object(self, active_object) -> None:  # todo: Pridat anotaciu, co je to active_object?
        self._active_objects.append(active_object)

    def remove_object(self, active_object) -> None:  # todo: Pridat anotaciu, co je to active_object?
        if active_object in self._active_objects:
            self._active_objects.remove(active_object)

    @property
    def picture_path(self):
        return self._picture_path