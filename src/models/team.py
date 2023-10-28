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
    Text,
)

from src.config.database import Base
from src.models.skill import Skill
from src.models.user import User


# TODO: разобраться с privacy
class Team(Base):
    __tablename__ = "team"
    __table_args__ = {"schema": "team"}

    uuid = Column(UUID, primary_key=True, unique=True, default=uuid.uuid4)
    owner_id = Column(UUID, ForeignKey(User.uuid), nullable=False)
    name = Column(String, nullable=False)
    image = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    member_description = Column(Text, nullable=True)
    privacy = Column(JSON, nullable=True)  # непанятна
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    deleted_at = Column(TIMESTAMP, nullable=True)


class UserTeam(Base):
    __tablename__ = "user_team"
    __table_args__ = {"schema": "team"}

    user_uuid = Column(UUID, ForeignKey(User.uuid), primary_key=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), primary_key=True)
    speciality = Column(String, nullable=True)


class TeamRole(Base):
    __tablename__ = "team_role"
    __table_args__ = {"schema": "team"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    name = Column(String, nullable=False)


class TeamPermission(Base):
    __tablename__ = "team_permission"
    __table_args__ = {"schema": "team"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class TeamRolePermission(Base):
    __tablename__ = "team_role_permission"
    __table_args__ = {"schema": "team"}

    role_id = Column(Integer, ForeignKey(TeamRole.id), primary_key=True)
    permission_id = Column(Integer, ForeignKey(TeamPermission.id), primary_key=True)
    value = Column(Boolean, nullable=False)


class TeamExperience(Base):
    __tablename__ = "team_experience"
    __table_args__ = {"schema": "team"}

    id = Column(Integer, primary_key=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    date_from = Column(TIMESTAMP, nullable=True)
    date_to = Column(TIMESTAMP, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


class AD(Base):
    __tablename__ = "ad"
    __table_args__ = {"schema": "team"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    speciality = Column(String, nullable=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_hide = Column(Boolean, nullable=False, default=False)
    is_promoting = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    deleted_at = Column(TIMESTAMP, nullable=True)


class ADSkill(Base):
    __tablename__ = "ad_skill"
    __table_args__ = {"schema": "team"}

    ad_id = Column(Integer, ForeignKey(AD.id), primary_key=True)
    skill_id = Column(Integer, ForeignKey(Skill.id), primary_key=True)
