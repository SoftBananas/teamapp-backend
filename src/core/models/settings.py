import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.annotated_types import uuid_pk
from src.core.models.base import Base
from src.core.models.user import User


class Settings(Base):
    __tablename__ = "settings"
    __table_args__ = {"schema": "settings"}

    id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(User.id, ondelete="CASCADE"), primary_key=True
    )
    is_notifying: Mapped[bool] = mapped_column(default=True)
    is_mailing: Mapped[bool] = mapped_column(default=True)


class Privacy(Base):
    __tablename__ = "privacy"
    __table_args__ = {"schema": "settings"}

    id: Mapped[uuid_pk]
    name: Mapped[str]
    slug: Mapped[str]


class UserPrivacy(Base):
    __tablename__ = "user_privacy"
    __table_args__ = {"schema": "settings"}

    user_uuid: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    privacy_id: Mapped[int] = mapped_column(primary_key=True)
