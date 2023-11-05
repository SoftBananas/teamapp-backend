import asyncio
import importlib
from types import ModuleType
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from src.config.config import Mode, config
from src.main import app

config = config.load(Mode.TEST)
importlib.import_module("src.models")
db = importlib.import_module("src.database")


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with db.engine.begin() as conn:
        await conn.run_sync(db.Base.metadata.create_all)
    yield
    async with db.engine.begin() as conn:
        await conn.run_sync(db.Base.metadata.drop_all)


# SETUP
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


sync_client = TestClient(app)


@pytest.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client
