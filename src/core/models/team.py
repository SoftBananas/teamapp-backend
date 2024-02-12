import datetime
import uuid
from typing import Any

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.annotated_types import created_at, int_pk, updated_at, uuid_pk
from src.core.models.base import Base
from src.core.models.skill import Skill
from src.core.models.user import User


# TODO: разобраться с privacy
class Team(Base):
    __tablename__ = "team"
    __table_args__ = {"schema": "team"}

    id: Mapped[uuid_pk]
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(User.id))
    name: Mapped[str]
    image: Mapped[str | None]
    description: Mapped[str | None]
    member_description: Mapped[str | None]
    privacy: Mapped[dict[str, Any] | None]  # непанятна
    created_at: Mapped[created_at]
    updated_at = Mapped[updated_at]
    deleted_at: Mapped[datetime.datetime | None]


class UserTeam(Base):
    __tablename__ = "user_team"
    __table_args__ = {"schema": "team"}

    user_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(User.id, ondelete="CASCADE"), primary_key=True
    )
    team_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(Team.id, ondelete="CASCADE"), primary_key=True
    )
    speciality: Mapped[str | None]


class TeamRole(Base):
    __tablename__ = "team_role"
    __table_args__ = {"schema": "team"}

    id: Mapped[int_pk]
    team_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(Team.id, ondelete="CASCADE")
    )
    speciality: Mapped[str | None]


class TeamPermission(Base):
    __tablename__ = "team_permission"
    __table_args__ = {"schema": "team"}

    id: Mapped[int_pk]
    name: Mapped[str]
    slug: Mapped[str]


class TeamRolePermission(Base):
    __tablename__ = "team_role_permission"
    __table_args__ = {"schema": "team"}

    role_id: Mapped[int] = mapped_column(
        ForeignKey(TeamRole.id, ondelete="CASCADE"), primary_key=True
    )
    permission_id: Mapped[int] = mapped_column(
        ForeignKey(TeamPermission.id, ondelete="CASCADE"), primary_key=True
    )
    value: Mapped[bool]


class TeamExperience(Base):
    __tablename__ = "team_experience"
    __table_args__ = {"schema": "team"}

    id: Mapped[int_pk]
    team_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(Team.id, ondelete="CASCADE")
    )
    date_from: Mapped[datetime.datetime | None]
    date_to: Mapped[datetime.datetime | None]
    name: Mapped[str]
    description: Mapped[str | None]


class Ad(Base):
    __tablename__ = "ad"
    __table_args__ = {"schema": "team"}

    id: Mapped[int_pk]
    team_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(Team.id, ondelete="CASCADE")
    )
    speciality: Mapped[str | None]
    name: Mapped[str]
    description: Mapped[str | None]
    is_hide: Mapped[bool] = mapped_column(default=False)
    is_promoting: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[created_at]
    updated_at = Mapped[updated_at]
    deleted_at: Mapped[datetime.datetime | None]


class AdSkill(Base):
    __tablename__ = "ad_skill"
    __table_args__ = {"schema": "team"}

    ad_id: Mapped[int] = mapped_column(
        ForeignKey(Ad.id, ondelete="CASCADE"), primary_key=True
    )
    skill_id: Mapped[int] = mapped_column(
        ForeignKey(Skill.id, ondelete="CASCADE"), primary_key=True
    )
