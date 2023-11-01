from typing import AsyncGenerator

from sqlalchemy import inspect, Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.core.config import config

if not config.is_loaded:
    raise Exception("Config was not loaded")

db = config.database
async_session_maker = db.session_maker


class Base(DeclarativeBase):
    metadata = db.metadata

    def get_dict(self) -> dict:
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self).mapper.column_attrs
        }


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with config.database.session_maker() as session:
        yield session
