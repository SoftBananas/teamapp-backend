from typing import Any, AsyncGenerator

from sqlalchemy import JSON, inspect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.config.config import config
from src.database.connection import Connection
from src.database.metadata_maker import MetadataMaker
from src.database.session_maker import SessionMaker

if not config.is_loaded:
    raise Exception("Config was not loaded")

__all__ = [
    "Base",
    "get_async_session",
    "engine",
    "connection",
    "session_maker"
]

connection = Connection(config)
engine = connection.engine

session_maker = SessionMaker(connection)
_metadata_maker = MetadataMaker(connection)


class Base(DeclarativeBase):
    metadata = _metadata_maker.metadata
    type_annotation_map = {dict[str, Any]: JSON}

    def get_dict(self) -> dict:
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self).mapper.column_attrs
        }


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session
