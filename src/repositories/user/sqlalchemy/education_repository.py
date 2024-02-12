from src.core.models import Education
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_education_repository import (
    AbstractEducationRepository,
)


class EducationSQLAlchemyRepository(SQLAlchemyRepository, AbstractEducationRepository):
    model_table = Education
