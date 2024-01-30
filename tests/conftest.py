from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from src.core.models.base import Base
from src.core.config.config import Mode, Config
from src.core.database import DataBase
from src.app import App

config = Config(Mode.TEST)
db = DataBase(config.database)
app = App(config)


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with db.connection.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with db.connection.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


sync_client = TestClient(app)


@pytest.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client
