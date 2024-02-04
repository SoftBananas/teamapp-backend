from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.core.database import DataBase
from src.core.models import Role, User
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyUserDatabase):
    model_table = User

    def __init__(self, database: DataBase):
        super().__init__(database.session_maker(), self.model_table)


class RoleRepository(SQLAlchemyRepository):
    model_table = Role
