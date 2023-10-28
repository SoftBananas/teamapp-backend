from enum import Enum

from yaml import safe_load

from config.config import Config


class Mode(Enum):
    DEV = "configs/dev.yml"
    TEST = "configs/test.yml"
    PROD = "configs/prod.yml"


def load_config(mode: Mode = Mode.PROD) -> Config:
    with open(f"{mode.value}", "r") as config_file:
        configs = safe_load(config_file)
    return Config(configs)
