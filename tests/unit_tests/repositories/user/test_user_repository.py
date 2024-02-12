import uuid

import pytest
from sqlalchemy import select

from repositories.user.sqlalchemy.user_repository import UserRepository
from src.core.models import User
from tests.conftest import db
from tests.unit_tests.repositories.utils import get_existing_models


@pytest.mark.asyncio(scope="class")
@pytest.mark.usefixtures("setup_database")
class TestUserRepository:
    async def test_add(self, user_models):
        for iteration, user in enumerate(user_models):
            repository = UserRepository(db)
            await repository.add(user)
            async with db.session_maker() as session:
                result = await session.execute(select(User))
                found_users = result.all()
                assert len(found_users) == iteration + 1
                assert found_users[iteration][0].username == user.username

    async def test_find_by_id(self):
        repository = UserRepository(db)
        existing_users = await get_existing_models(User)
        existing_uuids = [existing_user.id for existing_user in existing_users]
        for user_uuid in existing_uuids:
            found_user = await repository.find_by_id(user_uuid)
            assert isinstance(found_user, User)
            assert found_user.id == user_uuid

        not_existing_uuid = uuid.UUID(int=123)
        found_user = await repository.find_by_id(not_existing_uuid)
        assert found_user is None

    async def test_find_all(self):
        repository = UserRepository(db)
        found_user = await repository.find_all()
        assert isinstance(found_user, list)
        for user in found_user:
            assert isinstance(user, User)

    async def test_edit(self):
        existing_users = await get_existing_models(User)
        existing_uuids = [existing_user.id for existing_user in existing_users]
        repository = UserRepository(db)

        existing_user = await repository.find_by_id(existing_uuids[1])
        assert existing_user.role_id == 3

        existing_user.role_id = 2
        await repository.edit(existing_user)

        edited_user = await repository.find_by_id(existing_uuids[1])
        assert edited_user.role_id == 2
        not_edited_user = await repository.find_by_id(existing_uuids[0])
        assert not_edited_user.role_id == 1

    async def test_remove(self):
        existing_users = await get_existing_models(User)
        existing_uuids = [existing_user.id for existing_user in existing_users]
        repository = UserRepository(db)
        await repository.remove(existing_uuids[1])

        removed_user = await repository.find_by_id(existing_uuids[1])
        assert removed_user is None
        not_removed_user = await repository.find_by_id(existing_uuids[0])
        assert not_removed_user is not None

    async def test_remove_all(self, user_models):
        repository = UserRepository(db)
        await repository.add(user_models[1])
        existing_users = await get_existing_models(User)
        existing_uuids = [existing_user.id for existing_user in existing_users]

        await repository.remove_all()

        for removed_index in range(len(existing_users)):
            user = await repository.find_by_id(existing_uuids[removed_index])
            assert user is None
