from sqlalchemy import delete

from core.models import User
from core.schemas.user.role_schemas import RoleCreate
from core.schemas.user.user_schemas import UserCreate
from repositories.user_repositories import RoleRepository, UserRepository
from tests.conftest import db


async def add_role(role: RoleCreate):
    repository = RoleRepository(db)
    await repository.add(role)


async def remove_roles():
    repository = RoleRepository(db)
    await repository.remove_all()


async def remove_users():
    async with db.session_maker() as session:
        await session.execute(delete(User))
        await session.commit()


async def add_user(user: UserCreate):
    repository = UserRepository(db)
    await repository.add(user)
