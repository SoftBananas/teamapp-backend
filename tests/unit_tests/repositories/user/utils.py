from sqlalchemy import delete

from models import User
from repositories.user_repositories import RoleRepository, UserRepository
from schemas.user.role_schemas import RoleCreate
from schemas.user.user_schemas import UserCreate
from tests.conftest import db


async def add_role(role: RoleCreate):
    async with db.session_maker() as session:
        repository = RoleRepository(session=session)
        await repository.add(role)


async def remove_roles():
    async with db.session_maker() as session:
        repository = RoleRepository(session=session)
        await repository.remove_all()


async def remove_users():
    async with db.session_maker() as session:
        await session.execute(delete(User))
        await session.commit()


async def add_user(user: UserCreate):
    async with db.session_maker() as session:
        repository = UserRepository(session=session)
        await repository.add(user)
