class Field:

    __possible_fields_types = ['mountain', 'plains', 'forest', 'desert', 'water']

    def __init__(self, field_type, active_objects=None, properties=None):
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
        if field_type.lower() not in self.__possible_fields_types:
            raise ModuleNotFoundError(f'field type "{field_type}" not found\n Possible types are: {self.__possible_fields_types}')
        
        self.field_type = field_type
        self.properties = properties if properties else {}
        self.objects = []
        
        if active_objects is not None:
            self.objects.extend(object)

        self.player_present = False
        self.enemy_present = False

    def add_object(self, object):
        """
        Adds an object to the field.

        Parameters:
        - object: The object to be added.

        Returns:
        - None
        """
        self.objects.append(object)

    def remove_object(self, object):
        """
        Removes an object from the field.

        Parameters:
        - object: The object to be removed.

        Returns:
        - None
        """
        if object in self.objects:
            self.objects.remove(object)

    def player_presence(self, present):
        """
        Sets the presence of a player on the field.

        Parameters:
        - present (bool): True if a player is present, False otherwise.

        Returns:
        - None
        """
        self.player_present = present

    def enemy_presence(self, present):
        """
        Sets the presence of an enemy on the field.

        Parameters:
        - present (bool): True if an enemy is present, False otherwise.

        Returns:
        - None
        """
        self.enemy_present = present

# Example Usage:
field1 = Field("mountain", {"height": "high"})
field1.add_object("tree")
field1.player_presence(True)
field1.enemy_presence(False)

print("Type of the field:", field1.field_type)
print("Properties of the field:", field1.properties)
print("Objects on the field:", field1.objects)
print("Player present:", field1.player_present)
print("Enemy present:", field1.enemy_present)
