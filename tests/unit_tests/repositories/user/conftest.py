import pytest
from schemas.user.role_schemas import RoleCreate
from schemas.user.user_schemas import UserCreate


@pytest.fixture(scope="module")
def users():
    users = [
        UserCreate(
            name="Ivan",
            lastname="Vnukov",
            username="ONEPANTSU",
            email="conandet@mail.ru",
            hashed_password="12122002",
            role_id=1,
        ),
        UserCreate(
            name="Banana",
            lastname="Bananov",
            username="SoftySoft",
            email="teamapp@softbananas.com",
            hashed_password="12122002",
            role_id=3,
        ),
    ]
    return users


@pytest.fixture(scope="module")
def roles():
    users = [
        RoleCreate(name="Admin", slug="admin"),
        RoleCreate(name="Moderator", slug="moderator"),
        RoleCreate(name="User", slug="user"),
    ]
    return users
