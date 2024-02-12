from src.core.models import Notification
from src.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.repositories.user.abstract.abstract_notification_repository import (
    AbstractNotificationRepository,
)


class NotificationSQLAlchemyRepository(
    SQLAlchemyRepository, AbstractNotificationRepository
):
    model_table = Notification
