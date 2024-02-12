from src.core.models import ContactType
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_contact_type_repository import (
    AbstractContactTypeRepository,
)


class ContactTypeSQLAlchemyRepository(
    SQLAlchemyRepository, AbstractContactTypeRepository
):
    model_table = ContactType
