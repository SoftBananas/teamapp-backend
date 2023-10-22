from sqlalchemy import Column, VARCHAR, Integer

from src.database import Base, metadata


class Role(Base):
    __tablename__ = "role"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    event_id = Column(VARCHAR, nullable=False)
