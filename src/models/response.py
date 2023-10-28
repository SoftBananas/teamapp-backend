from sqlalchemy import Column, String, Integer, UUID, ForeignKey


from src.config.database import Base

from src.models.chat import Message
from src.models.team import Team
from src.models.user import CV


# RESPONSE MODULE
class ADResponse(Base):
    __tablename__ = "ad_response"

    id = Column(Integer, primary_key=True)
    user_uuid = Column(UUID, nullable=False)
    ad_id = Column(Integer, nullable=False)
    status_id = Column(Integer, nullable=False)


# message module
class MessageResponse(Base):
    __tablename__ = "message_response"

    message_id = Column(Integer, ForeignKey(Message.id), primary_key=True)
    response_id = Column(Integer, ForeignKey(ADResponse.id), primary_key=True)


class ResponseStatus(Base):
    __tablename__ = "response_status"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)


class CVResponse(Base):
    __tablename__ = "cv_response"

    id = Column(Integer, primary_key=True)
    team_uuid = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    cv_id = Column(Integer, ForeignKey(CV.id), nullable=False)
    status_id = Column(Integer, ForeignKey(ResponseStatus.id), nullable=False)


