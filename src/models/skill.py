from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base
from src.models.annotated_types import int_pk
from src.models.user import CV


class Skill(Base):
    __tablename__ = "skill"
    __table_args__ = {"schema": "skill"}

    id: Mapped[int_pk]
    name: Mapped[str]
    slug: Mapped[str]


class CVSkill(Base):
    __tablename__ = "cv_skill"
    __table_args__ = {"schema": "skill"}

    cv_id: Mapped[int] = mapped_column(
        ForeignKey(CV.id, ondelete="CASCADE"), primary_key=True
    )
    skill_id: Mapped[int] = mapped_column(
        ForeignKey(Skill.id, ondelete="CASCADE"), primary_key=True
    )


class Speciality(Base):
    __tablename__ = "speciality"
    __table_args__ = {"schema": "skill"}

    id: Mapped[int_pk]
    name: Mapped[str]
