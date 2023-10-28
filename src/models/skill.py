from sqlalchemy import Column, String, Integer, ForeignKey

from src.config.database import Base

from src.models.user import CV


# SKILL MODULE

class Skill(Base):
    __tablename__ = "skill"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class CVSkill(Base):
    __tablename__ = "cv_skill"

    cv_id = Column(Integer, ForeignKey(CV.id), primary_key=True)
    skill_id = Column(Integer, ForeignKey(Skill.id), primary_key=True)


class Speciality(Base):
    __tablename__ = "speciality"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)



