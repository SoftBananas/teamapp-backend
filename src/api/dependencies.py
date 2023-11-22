from src.repositories.user_repositories import UserRepository
from src.schemas.user.user_schemas import UserSchemasFabric
from src.services.user.user_service import UserService


def user_service():
    return UserService(UserRepository, UserSchemasFabric)
