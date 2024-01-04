import datetime
import enum
import uuid
from typing import Any

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base
from src.models.annotated_types import created_at, int_pk, updated_at, uuid_pk


class Role(Base):
    __tablename__ = "role"
    __table_args__ = {"schema": "user"}

    id: Mapped[int_pk]
    name: Mapped[str]
    slug: Mapped[str]


# TODO: разобраться с PgEnum
class Sex(enum.Enum):
    __table_args__ = {"schema": "user"}
    MALE = "male"
    FEMALE = "female"


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "user"}

    id: Mapped[uuid_pk]
    name: Mapped[str]
    lastname: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_verified: Mapped[bool] = mapped_column(default=False)
    role_id: Mapped[int] = mapped_column(ForeignKey(Role.id))
    image: Mapped[str | None]
    location: Mapped[dict[str, Any] | None]
    sex: Mapped[Sex | None]
    birthday: Mapped[datetime.date | None]

    created_at: Mapped[created_at]
    updated_at = Mapped[updated_at]
    deleted_at: Mapped[datetime.datetime | None]

    is_blocked: Mapped[bool] = mapped_column(default=False)


class CV(Base):
    __tablename__ = "cv"
    __table_args__ = {"schema": "user"}

    id: Mapped[int_pk]
    user_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(User.id, ondelete="CASCADE")
    )
    description: Mapped[str | None]


class ContactType(Base):
    __tablename__ = "contact_type"
    __table_args__ = {"schema": "user"}

    id: Mapped[int_pk]
    name: Mapped[str]
    slug: Mapped[str]


class CVContact(Base):
    __tablename__ = "cv_contact"
    __table_args__ = {"schema": "user"}

    cv_id: Mapped[int] = mapped_column(
        ForeignKey(CV.id, ondelete="CASCADE"), primary_key=True
    )
    contact_id: Mapped[int] = mapped_column(
        ForeignKey(ContactType.id, ondelete="CASCADE"), primary_key=True
    )

    contact_data: Mapped[str | None]
    is_preferred: Mapped[bool | None]


class Education(Base):
    __tablename__ = "education"
    __table_args__ = {"schema": "user"}

    id: Mapped[int_pk]
    cv_id: Mapped[int] = mapped_column(ForeignKey(CV.id, ondelete="CASCADE"))

    date_from: Mapped[datetime.datetime | None]
    date_to: Mapped[datetime.datetime | None]

    name: Mapped[str]
    description: Mapped[str | None]


class UserExperience(Base):
    __tablename__ = "user_experience"
    __table_args__ = {"schema": "user"}

    id: Mapped[int_pk]
    cv_id: Mapped[int] = mapped_column(ForeignKey(CV.id, ondelete="CASCADE"))

    date_from: Mapped[datetime.datetime | None]
    date_to: Mapped[datetime.datetime | None]

    name: Mapped[str]
    description: Mapped[str | None]


# TODO: обсудить, зачем нам это надо?
class Notification(Base):
    __tablename__ = "notification"
    __table_args__ = {"schema": "user"}

    id: Mapped[int_pk]
    user_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(User.id, ondelete="CASCADE")
    )
    image: Mapped[str | None]
    title: Mapped[str]
    description: Mapped[str | None]
    created_at: Mapped[created_at]
