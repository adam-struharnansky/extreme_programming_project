from effect import Effect
from item import Item

# todo - pridat kontrolu do kazdej set funkcie, ci je to spravneho typu


class Creature:
    def __init__(self,
                 health: int = 0,
                 attack: int = 0,
                 defence: int = 0,
                 evasion: int = 0,
                 equipment: list = None,
                 inventory: list = None,
                 effects: list = None) -> None:
        self._effects = effects if effects else []
        self._inventory = inventory if inventory else []  # todo - chceme mat stackovatelnu inventory?
        self._equipment = equipment if equipment else []  # todo - nechceme toto urobit zlozitejsie, rozdlit to na casti
        # aby sme mohli mat iba jeden mec, jeden stit..., ze by sme tu mali prava/lava ruka, hlava, telo, nohy, topanky
        self._health = health
        self._attack = attack
        self._defence = defence
        self._evasion = evasion

    def get_health(self) -> int:
        return self._health

    def set_health(self, new_health: int) -> None:
        self._health = new_health

    def change_health(self, health_difference: int) -> None:
        self._health += health_difference

    def get_attack(self) -> int:
        return self._attack

    def set_attack(self, new_attack: int) -> None:
        self._attack = new_attack

    def get_real_attack(self) -> int:
        """
        Computation of real attack - the combination of base attack with each item in equipment and each active effect.
        :return: Number representing the final attack.
        """
        real_attack = self.get_attack()
        # todo + pridat aj z equipmentu, porozmyslat ako budu fungovat komba
        # todo + pridat aj z efektov
        return real_attack

    def get_defence(self) -> int:
        return self._defence

    def get_real_defence(self) -> int:
        """
        Computation of real defence - the combination of base defence with each item in equipment and each active
        effect.
        :return:
        """
        real_defence = self.get_defence()
        # todo + pridat aj z equipmentu, porozmyslat ako budu fungovat komba
        # todo + pridat aj z efektov
        return real_defence

    def set_defence(self, new_defence: int) -> None:
        self._defence = new_defence

    def get_evasion(self) -> int:
        return self._evasion

    def set_evasion(self, new_evasion: int) -> None:
        self._evasion = new_evasion

    def get_equipment(self) -> list:
        return self._equipment

    def add_item_equipment(self, item: Item) -> bool:
        """
        Function to add item to equipment. If it is not possible to add item to equipment (equipment is full, the item
        was already inside), the function does nothing and returns False. If the item was successfully added then the
        function returns True.
        :param item: Item to be added
        :return: True if item was added, False otherwise
        """
        # todo - kontrola - ci to nie je None, ci je to spravny typ, ...
        # todo kontrola - nechceme mat naraz dva mece, atd
        self._equipment.append(item)
        return True

    def get_inventory(self) -> list:
        return self._inventory

    # todo pridat odobratie veci z inventory/equipmentu
    # todo pridat logiku na presunutie veci z inventory do equipmentu a naopak (ci uz pomocou funkcii alebo inak)

    def add_item_inventory(self, item: Item) -> bool:
        """
        Function to add item to equipment. If it is not possible to add item to inventory (inventory is full),
        the function does nothing and returns False. If the item was successfully added then the function returns True.
        :param item: Item to be added
        :return: True if item was added, False otherwise
        """
        # todo kontrola ci nie sme prilis plny
        self._inventory.append(item)
        return True

    def get_effects(self) -> list:
        return self._effects

    def add_effect(self, effect: Effect) -> None:
        # todo - porozmyslat ci mozeme mat viacnasobne ten isty effekt. Ak nie, pridat na to kontrolu
        self._effects.append(effect)

    def tick_effects(self) -> None:
        for effect in self._effects:
            # effect.tick()
            # todo
            pass

    def is_alive(self) -> bool:
        return self._health > 0