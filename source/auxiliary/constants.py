import os


AUXILIARY_DIRECTORY = os.path.dirname(__file__)
SOURCE_DIRECTORY = os.path.dirname(AUXILIARY_DIRECTORY)
PROJECT_DIRECTORY = os.path.dirname(SOURCE_DIRECTORY)
GRAPHIC_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'graphics')
DATA_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'data')
