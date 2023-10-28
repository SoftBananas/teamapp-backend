import os
from enum import Enum
from typing import Self

from dotenv import load_dotenv
from yaml import safe_load

from src.config.utils.singleton import MetaSingleton


class DataBase:
    def __init__(self):
        self.driver = os.environ.get("DB_DRIVER")
        self.host = os.environ.get("DB_HOST")
        self.port = os.environ.get("DB_PORT")
        self.name = os.environ.get("DB_NAME")
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASSWORD")

    def get_url(self):
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Mode(Enum):
    DEV = "configs/dev.yml"
    TEST = "configs/test.yml"
    PROD = "configs/prod.yml"


class Config(metaclass=MetaSingleton):
    configs: dict
    database: DataBase
    origins: list[str]

    def load(self, mode: Mode = Mode.PROD) -> Self:
        with open(f"{mode.value}", "r") as config_file:
            configs = safe_load(config_file)
        return self.set_configs(configs)

    def set_configs(self, configs: dict) -> Self:
        if configs is None:
            raise ValueError("YAML file not given")
        self.configs = configs
        load_dotenv(self.configs["env_file"])

        self.database = DataBase()
        self.origins = self.configs["origins"]

        return self


config = Config()
