from src.core.models import CVContact
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_cv_contact_repository import (
    AbstractCVContactRepository,
)


class CVContactSQLAlchemyRepository(SQLAlchemyRepository, AbstractCVContactRepository):
    model_table = CVContact
