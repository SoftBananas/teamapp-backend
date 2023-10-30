import os
from typing import Any, AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import NullPool


class DataBase:
    metadata: MetaData
    engine: AsyncEngine
    Base: Any

    def __init__(self):
        self._set_connection()
        self._set_metadata()
        self._set_session_maker()
        self._set_base()

    def get_url(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    def _set_connection(self) -> None:
        self.driver = os.environ.get("DB_DRIVER")
        self.host = os.environ.get("DB_HOST")
        self.port = os.environ.get("DB_PORT")
        self.name = os.environ.get("DB_NAME")
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASSWORD")

    def _set_metadata(self) -> None:
        self.metadata = MetaData()
        self.engine = create_async_engine(url=self.get_url(), poolclass=NullPool)
        self.metadata.bind = self.engine

    def _set_session_maker(self) -> None:
        self.session_maker = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    def _set_base(self) -> None:
        self.Base = DeclarativeBase
        self.Base.metadata = self.metadata
