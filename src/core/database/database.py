from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from src.core.config.config import Config
from src.core.database.connection import Connection
from src.core.database.session_maker import SessionMaker


class DataBase:
    def __init__(self, config: Config):
        self.config = config
        self.connection = Connection(config)
        self.session_maker = SessionMaker(self.connection)

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:
            yield session
