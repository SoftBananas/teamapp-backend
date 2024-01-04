from src.core.database import DataBase
from src.core.schemas.user.user_schemas import UserSchemasFabric
from src.repositories.user_repositories import UserRepository
from src.services.user.user_service import UserService


def user_service(database: DataBase) -> UserService:
    return UserService(UserRepository, UserSchemasFabric)
