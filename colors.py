from field import FieldType


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WATER = (0, 0, 255)
GROUND = (139, 69, 19)
MOUNTAINS = (128, 128, 128)
PLAYER_COLOR = (100, 200, 50)
ENEMY_COLOR = (255, 0, 0)


def get_field_color(field_type):
    match field_type:
        case FieldType.MOUNTAIN:
            return MOUNTAINS
        case FieldType.DESERT:
            return YELLOW
        case FieldType.PLAINS:
            return GROUND
        case FieldType.FOREST:
            return GREEN
        case FieldType.WATER:
            return BLUE
    return BLACK  # todo
