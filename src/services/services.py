from src.repositories.repositories import Repositories
from src.services.user import *
from src.utils.auth_core import AuthCore


class Services:
    def __init__(self, repositories: Repositories, auth_core: AuthCore) -> None:
        self.user_service = UserService(
            repositories.user_repositories.user_repository, auth_core
        )
        # self.example_service = UserService(repositories.user_repository)
