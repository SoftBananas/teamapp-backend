from src.core.models import UserExperience
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_user_experience_repository import (
    AbstractUserExperienceRepository,
)


class UserExperienceSQLAlchemyRepository(
    SQLAlchemyRepository, AbstractUserExperienceRepository
):
    model_table = UserExperience
