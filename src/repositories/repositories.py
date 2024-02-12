from src.core.database import DataBase
from src.repositories.user.user_repositories import UserRepositories


class Repositories:

    def __init__(self, database: DataBase) -> None:
        self.user_repositories = UserRepositories(database)
