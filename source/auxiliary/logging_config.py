import logging
import sys


def setup_logging(level=logging.DEBUG,
                  format_str="[%(levelname)s] - %(asctime)s - %(filename)s:%(lineno)d - %(message)s"):
    logging.basicConfig(level=level, format=format_str, stream=sys.stdout)
