from models import Role, User
from repositories.sqlalchemy_repository import SQLAlchemyRepository
from schemas.user.role_schemas import RoleSchemas
from schemas.user.user_schemas import UserSchemas


class UserRepository(SQLAlchemyRepository):
    model = User
    schemas = UserSchemas()


class RoleRepository(SQLAlchemyRepository):
    model = Role
    schemas = RoleSchemas()
