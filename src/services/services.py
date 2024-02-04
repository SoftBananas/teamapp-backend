from src.core.config import Config
from src.core.database import DataBase
from src.repositories.repositories import Repositories
from src.services.user import *


class Services:
    def __init__(
        self, repositories: Repositories, config: Config
    ) -> None:
        self.user_service = UserService(repositories.user_repository, config.auth)
        # self.example_service = UserService(repositories.user_repository)
