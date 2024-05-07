
import os
import random

from dataclasses import dataclass, field

from source.auxiliary import ItemLevel
from source.game.items import generate_random_item


@dataclass
class Loot:
    item_level: ItemLevel = field(default_factory=lambda: random.choice(list(ItemLevel)))

    def __post_init__(self):
        match self.item_level:
            case ItemLevel.BRONZE:
                self._picture_path = os.path.join('items', 'loot_chests', 'loot_bronze.png')
            case ItemLevel.SILVER:
                self._picture_path = os.path.join('items', 'loot_chests', 'loot_silver.png')
            case ItemLevel.GOLD:
                self._picture_path = os.path.join('items', 'loot_chests', 'loot_gold.png')
            case ItemLevel.LEGENDARY:
                self._picture_path = os.path.join('items', 'loot_chests', 'loot_legendary.png')

    def get_item(self):
        return generate_random_item(self.item_level)

    @property
    def picture_path(self):
        return self._picture_path
