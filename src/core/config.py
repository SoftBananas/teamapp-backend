from enum import Enum
from typing import Self

from dotenv import load_dotenv
from yaml import safe_load

from src.core.database import DataBase


class Mode(Enum):
    DEV = "configs/dev.yml"
    TEST = "configs/test.yml"
    PROD = "configs/prod.yml"


class _Config:
    configs: dict
    database: DataBase
    origins: list[str]

    def __init__(self):
        self.is_loaded = False

    def load(self, mode: Mode = Mode.PROD) -> Self:
        with open(f"{mode.value}", "r") as config_file:
            configs = safe_load(config_file)
        self._set_configs(configs)
        self.is_loaded = True
        return self

    def _set_configs(self, configs: dict) -> Self:
        if configs is None:
            raise ValueError("YAML file not given")
        self.configs = configs
        load_dotenv(self.configs["env_file"])

        self._set_database()
        self._set_origins()

    def _set_database(self) -> str:
        self.database = DataBase()

    def _set_origins(self):
        self.origins = self.configs["origins"]


config = _Config()
