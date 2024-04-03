import random


class Field:

    __possible_fields_types = ['mountain', 'plains', 'forest', 'desert', 'water']

    def __init__(self, field_type=None, active_objects=None, properties=None):
        """
        Initializes a new instance of the Field class.

        Parameters:
        - field_type (str): The type of the field (e.g., mountains, plains, forest, desert, water, ...).
        - properties (dict): Optional. Properties associated with the field.
        - active_object (list of (obj - not implemented yet)): Optional. objects active in this field

        Returns:
        - object field
        """

        # check if field type is correct
        if field_type is not None and field_type.lower() not in self.__possible_fields_types:
            raise ModuleNotFoundError(f'field type "{field_type}" not found\n Possible types are: {self.__possible_fields_types}')
        
        self._field_type = field_type if field_type else random.choice(self.__possible_fields_types)
        self._properties = properties if properties else {}
        self._objects = []
        
        if active_objects is not None:
            self.objects.extend(active_objects)

        self._enemy_present = False
        self._player_present = False

    def __eq__(self, other):
        if other is None or not isinstance(other, Field):
            return False
        if self._field_type != other.get_fiel_type():
            return False
        if self._properties != other.get_properties():
            return False
        if self._objects != other.get_objects():
            return False
        if self._enemy_present != other.is_enemy_present():
            return False
        if self._player_present != other.is_player_present():
            return False
        
        return True

    def get_field_type(self):
        return self._field_type

    def get_properties(self):
        return self._properties

    def get_objects(self):
        return self._objects

    def is_player_present(self):
        return self._player_present

    def is_enemy_present(self):
        return self._enemy_present

    def add_object(self, object):
        """
        Adds an object to the field.

        Parameters:
        - object: The object to be added.

        Returns:
        - None
        """
        self._objects.append(object)

    def remove_object(self, object):
        """
        Removes an object from the field.

        Parameters:
        - object: The object to be removed.

        Returns:
        - None
        """
        if object in self._objects:
            self._objects.remove(object)

    def set_player_presence(self, present):
        """
        Sets the presence of a player on the field.

        Parameters:
        - present (bool): True if a player is present, False otherwise.

        Returns:
        - None
        """
        self._player_present = present

    def enemy_presence(self, present):
        """
        Sets the presence of an enemy on the field.

        Parameters:
        - present (bool): True if an enemy is present, False otherwise.

        Returns:
        - None
        """
        self._enemy_present = present
