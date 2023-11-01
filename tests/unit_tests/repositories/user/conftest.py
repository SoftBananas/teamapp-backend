import json

import pytest
from pydantic import BaseModel

from models import User, Role
from src.schemas.user.role_schemas import RoleCreate
from src.schemas.user.user_schemas import UserCreate

from unit_tests.repositories.user.utils import add_role, remove_roles, remove_users


@pytest.fixture(scope="session")
def user_schemas() -> list[BaseModel]:
    json_users = json.load(open("tests/unit_tests/repositories/user/test_data.json"))["users"]
    users = [UserCreate(**json_user) for json_user in json_users]
    return users


@pytest.fixture(scope="session")
def user_models(user_schemas) -> list[User]:
    users = [User(**user_schema.model_dump())
             for user_schema in user_schemas]
    return users


@pytest.fixture(scope="session")
def role_schemas() -> list[RoleCreate]:
    json_roles = json.load(open("tests/unit_tests/repositories/user/test_data.json"))["roles"]
    users = [RoleCreate(**json_role) for json_role in json_roles]
    return users


@pytest.fixture(scope="session")
def role_models(role_schemas) -> list[Role]:
    users = [Role(**role_schema.model_dump())
             for role_schema in role_schemas]
    return users


@pytest.fixture(scope="module")
async def setup_database(role_models):
    for role in role_models:
        await add_role(role)
    yield
    await remove_users()
    await remove_roles()
