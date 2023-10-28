from sqlalchemy import VARCHAR, Column, Integer

from src.config.database import Base


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    event_id = Column(VARCHAR, nullable=False)
