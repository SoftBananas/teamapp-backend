from sqlalchemy import Column, String, Integer, UUID, Boolean, ForeignKey

from src.config.database import Base

from src.models.user import User


# ----- SETTINGS MODULE -----
class Settings(Base):
    __tablename__ = "settings"

    user_uuid = Column(UUID, ForeignKey(User.uuid), primary_key=True)
    is_notifying = Column(Boolean, nullable=False, default=True)
    is_mailing = Column(Boolean, nullable=False, default=True)


class Privacy(Base):
    __tablename__ = "privacy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class UserPrivacy(Base):
    __tablename__ = "user_privacy"

    user_uuid = Column(UUID, primary_key=True)
    privacy_id = Column(Integer, primary_key=True)
