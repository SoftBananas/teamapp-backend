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
    database: DataBaseConfig
    app: AppConfig
    origins: list[str]

    def __init__(self, mode: Mode | None = None) -> Self:
        if mode is None:
            self.is_loaded = False
        else:
            self._set_configs(mode)
            self.is_loaded = True

    def _set_configs(self, mode: Mode = Mode.PROD) -> Self:
        with open(f"{mode.value}", "r") as config_file:
            configs = safe_load(config_file)
        load_dotenv(configs["env_file"])
        self.set_app(configs["app"])
        self.set_database(configs["database"])
        self.set_logger(configs["logger"])
        self.set_origins(configs["origins"])

    def set_app(self, app_config: dict):
        self.app = AppConfig(
            title=app_config["title"],
            version=app_config["version"],
            host=app_config["host"],
            port=app_config["port"],
        )

    def set_database(self, db_config: dict):
        self.database = DataBaseConfig(
            driver=db_config["driver"],
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            name=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
        )

    def set_logger(self, logger_config: dict):
        logger.remove()
        logger.add(
            sink=logger_config["sink"],
            format=logger_config["format"],
            level=logger_config["level"],
            rotation=logger_config["rotation"],
            compression=logger_config["compression"],
        )

    def set_origins(self, origins_config: dict):
        self.origins = origins_config
