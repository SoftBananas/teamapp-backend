import enum
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models.annotated_types import int_pk
from src.core.models.base import Base
from src.core.models.chat import Message
from src.core.models.team import Team
from src.core.models.user import CV


class AdStatus(enum.Enum):
    RECALL = "recall"
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class AdResponse(Base):
    __tablename__ = "ad_response"
    __table_args__ = {"schema": "response"}

    id: Mapped[int_pk]
    user_uuid: Mapped[uuid.UUID]
    ad_id: Mapped[int]
    status_id: Mapped[AdStatus]


# message module
class MessageResponse(Base):
    __tablename__ = "message_response"
    __table_args__ = {"schema": "response"}

    message_id: Mapped[int] = mapped_column(ForeignKey(Message.id), primary_key=True)
    response_id: Mapped[int] = mapped_column(
        ForeignKey(AdResponse.id, ondelete="CASCADE"), primary_key=True
    )


class ResponseStatus(Base):
    __tablename__ = "response_status"
    __table_args__ = {"schema": "response"}

    id: Mapped[int_pk]
    name: Mapped[str]
    slug: Mapped[str]


class CVResponse(Base):
    __tablename__ = "cv_response"
    __table_args__ = {"schema": "response"}

    id: Mapped[int_pk]
    team_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(Team.id, ondelete="CASCADE")
    )
    cv_id: Mapped[int] = mapped_column(ForeignKey(CV.id))
    status_id: Mapped[int] = mapped_column(ForeignKey(ResponseStatus.id))
