from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.core.database.connection import Connection


class SessionMaker:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.session_maker = sessionmaker(
            self.connection.engine, class_=AsyncSession, expire_on_commit=False
        )

    def __call__(self):
        return self.session_maker()
