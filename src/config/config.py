import os

from dotenv import load_dotenv

from config.utils import MetaSingleton


class DataBase:
    def __init__(self):
        self.driver = os.environ.get("DB_DRIVER")
        self.host = os.environ.get("DB_HOST")
        self.port = os.environ.get("DB_PORT")
        self.name = os.environ.get("DB_NAME")
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASSWORD")


class Config(metaclass=MetaSingleton):
    database: DataBase
    origins = list[str]

    def __init__(self, configs: dict = None):
        if configs is None:
            raise ValueError("YAML file not given")
        self.configs = configs
        load_dotenv(self.configs["env_file"])

        self.database = DataBase()
        self.origins = self.configs["origins"]
