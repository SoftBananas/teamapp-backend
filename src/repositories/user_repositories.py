from models import Role, User
from repositories.sqlalchemy_repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model_table = User
    model = model_table()


class RoleRepository(SQLAlchemyRepository):
    model_table = Role
    model = model_table()
