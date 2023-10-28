from sqlalchemy import UUID, Boolean, Column, ForeignKey, Integer, String

from src.config.database import Base
from src.models.user import User


class Settings(Base):
    __tablename__ = "settings"
    __table_args__ = {"schema": "settings"}

    user_uuid = Column(UUID, ForeignKey(User.uuid), primary_key=True)
    is_notifying = Column(Boolean, nullable=False, default=True)
    is_mailing = Column(Boolean, nullable=False, default=True)


class Privacy(Base):
    __tablename__ = "privacy"
    __table_args__ = {"schema": "settings"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class UserPrivacy(Base):
    __tablename__ = "user_privacy"
    __table_args__ = {"schema": "settings"}

    user_uuid = Column(UUID, primary_key=True)
    privacy_id = Column(Integer, primary_key=True)
