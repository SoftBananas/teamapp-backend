from datetime import datetime

from sqlalchemy import Column, String, Integer, UUID, Boolean, ForeignKey, JSON, DATETIME, DATE

from src.config.database import Base

import uuid


class User(Base):
    __tablename__ = "user"

    uuid = Column(UUID, primary_key=True, unique=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    image = Column(String, nullable=True)
    location = Column(JSON, nullable=True)
    sex = Column(String, nullable=True)
    birthday = Column(DATE, nullable=True)

    created_at = Column(DATETIME, nullable=False, default=datetime.now())
    updated_at = Column(DATETIME, nullable=False)
    deleted_at = Column(DATETIME, nullable=True)
    is_blocked = Column(Boolean, nullable=False)


class CV(Base):
    __tablename__ = "cv"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_uuid = Column(UUID, ForeignKey(User.uuid), nullable=False)
    description = Column(String, nullable=True)


class ContactType(Base):
    __tablename__ = "contact_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class CVContact(Base):
    __tablename__ = "cv_contact"

    cv_id = Column(Integer, ForeignKey(CV.id), primary_key=True)
    contact_id = Column(Integer, ForeignKey(ContactType.id), primary_key=True)

    contact_data = Column(String, nullable=True)
    is_preferred = Column(Boolean, nullable=True)


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cv_id = Column(Integer, ForeignKey(CV.id), nullable=False)

    date_from = Column(DATE, nullable=True)
    date_to = Column(DATE, nullable=True)

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


class UserExperience(Base):
    __tablename__ = "user_experience"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cv_id = Column(Integer, ForeignKey(CV.id), nullable=False)

    date_from = Column(DATE, nullable=True)
    date_to = Column(DATE, nullable=False)

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


# TODO: обсудить, зачем нам это надо?
class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True)
    user_uuid = Column(UUID, ForeignKey(User.uuid), nullable=False)
    image = Column(Integer, nullable=True)
    created_at = Column(DATETIME, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
