import os

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine

from src.config.config import Config


class Connection:

    def __init__(self, config: Config):
        self.db = config.database
        self.engine = self.__create_engine()

    def get_url(self) -> str:
        return f"{self.db.driver}://{self.db.user}:{self.db.password}@{self.db.host}:{self.db.port}/{self.db.name}"

    def __create_engine(self):
        return create_async_engine(url=self.get_url(), poolclass=NullPool)
