from datetime import datetime

from sqlalchemy import Column, String, Integer, UUID, Boolean, ForeignKey, JSON, DATETIME, DATE, Float, Text

from src.config.database import Base

import uuid

from src.models.user import User
from src.models.skill import Skill


# TEAM MODULE

# TODO: разобраться с privacy
class Team(Base):
    __tablename__ = "team"

    uuid = Column(UUID, primary_key=True, unique=True, default=uuid.uuid4)
    owner_id = Column(UUID, ForeignKey(User.uuid), nullable=False)
    name = Column(String, nullable=False)
    image = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    member_description = Column(Text, nullable=True)
    privacy = Column(JSON, nullable=True)  # непанятна
    created_at = Column(DATETIME, nullable=False, default=datetime.now())
    updated_at = Column(DATETIME, nullable=False, default=datetime.now())
    deleted_at = Column(DATETIME, nullable=True)


class UserTeam(Base):
    __tablename__ = "user_team"

    user_uuid = Column(UUID, ForeignKey(User.uuid), primary_key=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), primary_key=True)
    speciality = Column(String, nullable=True)


class TeamRole(Base):
    __tablename__ = "team_role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    name = Column(String, nullable=False)


class TeamPermission(Base):
    __tablename__ = "team_permission"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class TeamRolePermission(Base):
    __tablename__ = "team_role_permission"

    role_id = Column(Integer, ForeignKey(TeamRole.id), primary_key=True)
    permission_id = Column(Integer, ForeignKey(TeamPermission.id), primary_key=True)
    value = Column(Boolean, nullable=False)


class TeamExperience(Base):
    __tablename__ = "team_experience"

    id = Column(Integer, primary_key=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    date_from = Column(DATE, nullable=True)
    date_to = Column(DATE, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


class AD(Base):
    __tablename__ = "ad"

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    speciality = Column(String, nullable=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_hide = Column(Boolean, nullable=False, default=False)
    is_promoting = Column(Boolean, nullable=False, default=False)
    created_at = Column(DATETIME, nullable=False, default=datetime.now())
    updated_at = Column(DATETIME, nullable=False, default=datetime.now())
    deleted_at = Column(DATETIME, nullable=True)


class ADSkill(Base):
    __tablename__ = "ad_skill"

    ad_id = Column(Integer, ForeignKey(AD.id), primary_key=True)
    skill_id = Column(Integer, ForeignKey(Skill.id), primary_key=True)