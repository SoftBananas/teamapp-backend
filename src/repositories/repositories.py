from src.core.database import DataBase
from src.repositories.user_repositories import UserRepository


class Repositories:
    def __init__(self, database: DataBase) -> None:
        self.user_repository = UserRepository(database)
