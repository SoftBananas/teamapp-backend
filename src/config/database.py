from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool

from src.config.config import config

DATABASE_URL = config.database.get_url()

metadata = MetaData()
Base = declarative_base(metadata=metadata)

engine = create_async_engine(url=DATABASE_URL, poolclass=NullPool)
async_session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

metadata.bind = engine


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
