from src.core.models import Role
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_role_repository import (
    AbstractRoleRepository,
)


class RoleSQLAlchemyRepository(SQLAlchemyRepository, AbstractRoleRepository):
    model_table = Role
