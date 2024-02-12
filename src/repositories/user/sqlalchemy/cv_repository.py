from src.core.models import CV
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_cv_repository import AbstractCVRepository


class CVSQLAlchemyRepository(SQLAlchemyRepository, AbstractCVRepository):
    model_table = CV
