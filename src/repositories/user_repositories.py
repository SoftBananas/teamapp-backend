from src.models import Role, User
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model_table = User


class RoleRepository(SQLAlchemyRepository):
    model_table = Role
