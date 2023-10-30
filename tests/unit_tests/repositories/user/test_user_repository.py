import uuid

import pytest
from repositories.user_repositories import UserRepository
from schemas.user.user_schemas import UserRead
from sqlalchemy import select
from src.models import User
from tests.conftest import db

from unit_tests.repositories.user.utils import add_role, remove_roles, remove_users


@pytest.fixture(autouse=True, scope="module")
async def setup_database(roles):
    for role in roles:
        await add_role(role)
    yield
    await remove_users()
    await remove_roles()


@pytest.mark.usefixtures("setup_database")
class TestUserRepository:
    async def test_add(self, users):
        for iteration, user in enumerate(users):
            async with db.session_maker() as session:
                repository = UserRepository(session=session)
                await repository.add(user)

            async with db.session_maker() as session:
                result = await session.execute(select(User))
                found_users = result.all()
                assert len(found_users) == iteration + 1
                assert found_users[iteration][0].username == user.username

    async def test_find_by_id(self):
        async with db.session_maker() as session:
            repository = UserRepository(session=session)

            for user_uuid in await self.__get_existing_uuids():
                found_user = await repository.find_by_id(user_uuid)
                assert isinstance(found_user, UserRead)
                assert found_user.id == user_uuid

            not_existing_uuid = uuid.UUID(int=123)
            found_user = await repository.find_by_id(not_existing_uuid)
            assert found_user is None

    async def test_find_all(self):
        async with db.session_maker() as session:
            repository = UserRepository(session=session)
            found_user = await repository.find_all()
            assert isinstance(found_user, list)
            for user in found_user:
                assert isinstance(user, UserRead)

    async def test_edit(self):
        uuids = await self.__get_existing_uuids()
        async with db.session_maker() as session:
            repository = UserRepository(session=session)

            user = await repository.find_by_id(uuids[1])
            assert user.role_id == 3
            user.role_id = 2
            await repository.edit(user)
            user = await repository.find_by_id(uuids[1])
            assert user.role_id == 2

            user = await repository.find_by_id(uuids[0])
            assert user.role_id == 1

    async def test_remove(self):
        uuids = await self.__get_existing_uuids()
        async with db.session_maker() as session:
            repository = UserRepository(session=session)
            await repository.remove(uuids[1])
            user = await repository.find_by_id(uuids[1])
            assert user is None
            user = await repository.find_by_id(uuids[0])
            assert user is not None

    async def test_remove_all(self, users):
        async with db.session_maker() as session:
            repository = UserRepository(session=session)
            await repository.add(users[1])
            uuids = await self.__get_existing_uuids()
            await repository.remove_all()
            user = await repository.find_by_id(uuids[1])
            assert user is None
            user = await repository.find_by_id(uuids[0])
            assert user is None

    @staticmethod
    async def __get_existing_uuids() -> list[uuid.UUID]:
        async with db.session_maker() as session:
            result = await session.execute(select(User))
            uuids = [user[0].id for user in result.all()]
        return uuids
