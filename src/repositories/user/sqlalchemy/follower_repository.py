from src.core.models import Follower
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_follower_repository import (
    AbstractFollowerRepository,
)


class FollowerSQLAlchemyRepository(SQLAlchemyRepository, AbstractFollowerRepository):
    model_table = Follower
