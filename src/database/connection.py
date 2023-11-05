import os

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine

from src.config.config import Config


class Connection:
    driver: str
    host: str
    port: int
    name: str
    user: str
    password: str

    def __init__(self, config: Config):
        self.config = config
        self.__set_connection()
        self.engine = self.__create_engine()

    def get_url(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    def __set_connection(self) -> None:
        self.driver = os.environ.get("DB_DRIVER")
        self.host = os.environ.get("DB_HOST")
        self.port = os.environ.get("DB_PORT")
        self.name = os.environ.get("DB_NAME")
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASSWORD")

    def __create_engine(self):
        return create_async_engine(url=self.get_url(), poolclass=NullPool)
