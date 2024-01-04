from src.repositories.repositories import Repositories
from src.services.user.user_service import UserService


class Services:
    def __init__(self, repositories: Repositories) -> None:
        self.user_service = UserService(repositories.user_repository)

