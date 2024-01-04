import os
from enum import Enum
from typing import Self

from dotenv import load_dotenv
from loguru import logger
from yaml import safe_load

from src.core.config.app_config import AppConfig
from src.core.config.database_config import DataBaseConfig


class Mode(Enum):
    DEV = "configs/dev.yml"
    TEST = "configs/test.yml"
    PROD = "configs/prod.yml"


class Config:
    configs: dict
    database: DataBaseConfig
    app: AppConfig
    origins: list[str]

    def __init__(self, mode: Mode | None = None) -> Self:
        if mode is None:
            self.is_loaded = False
        else:
            self._set_configs(mode)
            self.is_loaded = True

    def load(self, mode: Mode = Mode.PROD) -> Self:
        self._set_configs(mode)
        self.is_loaded = True
        return self

    def _set_configs(self, mode: Mode = Mode.PROD) -> Self:
        with open(f"{mode.value}", "r") as config_file:
            self.configs = safe_load(config_file)
        load_dotenv(self.configs["env_file"])
        self.set_app()
        self.set_database()
        self.set_logger()
        self.set_origins()

    def set_app(self):
        self.app = AppConfig(
            host=self.configs["app"]["host"],
            port=self.configs["app"]["port"],
        )

    def set_database(self):
        self.database = DataBaseConfig(
            driver=self.configs["database"]["driver"],
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            name=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
        )

    def set_logger(self):
        logger_configs = self.configs["logger"]
        logger.remove()
        logger.add(
            sink=logger_configs["sink"],
            format=logger_configs["format"],
            level=logger_configs["level"],
            rotation=logger_configs["rotation"],
            compression=logger_configs["compression"],
        )

    def set_origins(self):
        self.origins = self.configs["origins"]


config = Config()
