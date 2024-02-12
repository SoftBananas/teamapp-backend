from src.core.database import DataBase
from src.repositories.user.abstract import *
from src.repositories.user.sqlalchemy import *


class UserRepositories:

    def __init__(self, database: DataBase) -> None:
        self.user_repository: AbstractUserRepository = UserSQLAlchemyRepository(
            database
        )
        self.user_experience_repository: AbstractUserExperienceRepository = (
            UserExperienceSQLAlchemyRepository(database)
        )
        self.role_repository: AbstractRoleRepository = RoleSQLAlchemyRepository(
            database
        )
        self.contact_type_repository: AbstractContactTypeRepository = (
            ContactTypeSQLAlchemyRepository(database)
        )
        self.cv_contact_repository: AbstractCVContactRepository = (
            CVContactSQLAlchemyRepository(database)
        )
        self.notification_repository: AbstractNotificationRepository = (
            NotificationSQLAlchemyRepository(database)
        )
        self.education_repository: AbstractEducationRepository = (
            EducationSQLAlchemyRepository(database)
        )
        self.follower_repository: AbstractFollowerRepository = (
            FollowerSQLAlchemyRepository(database)
        )
