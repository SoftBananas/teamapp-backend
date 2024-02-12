import uuid

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.core.database import DataBase
from src.core.models import User
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_user_repository import (
    AbstractUserRepository,
)


class UserSQLAlchemyRepository(
    SQLAlchemyUserDatabase, SQLAlchemyRepository, AbstractUserRepository
):
    model_table = User

    def __init__(self, database: DataBase):
        super().__init__(database.session_maker(), self.model_table)
