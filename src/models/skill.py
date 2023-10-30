from sqlalchemy import Column, ForeignKey, Integer, String

from src.database import Base
from src.models.user import CV


class Skill(Base):
    __tablename__ = "skill"
    __table_args__ = {"schema": "skill"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class CVSkill(Base):
    __tablename__ = "cv_skill"
    __table_args__ = {"schema": "skill"}

    cv_id = Column(Integer, ForeignKey(CV.id), primary_key=True)
    skill_id = Column(Integer, ForeignKey(Skill.id), primary_key=True)


class Speciality(Base):
    __tablename__ = "speciality"
    __table_args__ = {"schema": "skill"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
