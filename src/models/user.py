import uuid
from datetime import datetime

from sqlalchemy import (
    TIMESTAMP,
    JSON,
    UUID,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)

from src.config.database import Base


class Role(Base):
    __tablename__ = "role"
    __table_args__ = {"schema": "user"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "user"}

    uuid = Column(UUID, primary_key=True, unique=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)
    role_id = Column(Integer, ForeignKey(Role.id), nullable=False)
    image = Column(String, nullable=True)
    location = Column(JSON, nullable=True)
    sex = Column(String, nullable=True)
    birthday = Column(TIMESTAMP, nullable=True)

    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=False)
    deleted_at = Column(TIMESTAMP, nullable=True)
    is_blocked = Column(Boolean, nullable=False)


class CV(Base):
    __tablename__ = "cv"
    __table_args__ = {"schema": "user"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_uuid = Column(UUID, ForeignKey(User.uuid), nullable=False)
    description = Column(String, nullable=True)


class ContactType(Base):
    __tablename__ = "contact_type"
    __table_args__ = {"schema": "user"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class CVContact(Base):
    __tablename__ = "cv_contact"
    __table_args__ = {"schema": "user"}

    cv_id = Column(Integer, ForeignKey(CV.id), primary_key=True)
    contact_id = Column(Integer, ForeignKey(ContactType.id), primary_key=True)

    contact_data = Column(String, nullable=True)
    is_preferred = Column(Boolean, nullable=True)


class Education(Base):
    __tablename__ = "education"
    __table_args__ = {"schema": "user"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    cv_id = Column(Integer, ForeignKey(CV.id), nullable=False)

    date_from = Column(TIMESTAMP, nullable=True)
    date_to = Column(TIMESTAMP, nullable=True)

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


class UserExperience(Base):
    __tablename__ = "user_experience"
    __table_args__ = {"schema": "user"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    cv_id = Column(Integer, ForeignKey(CV.id), nullable=False)

    date_from = Column(TIMESTAMP, nullable=True)
    date_to = Column(TIMESTAMP, nullable=False)

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


# TODO: обсудить, зачем нам это надо?
class Notification(Base):
    __tablename__ = "notification"
    __table_args__ = {"schema": "user"}

    id = Column(Integer, primary_key=True)
    user_uuid = Column(UUID, ForeignKey(User.uuid), nullable=False)
    image = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
