import datetime
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base
from src.models.annotated_types import created_at, int_pk, updated_at


class Chat(Base):
    __tablename__ = "chat"
    __table_args__ = {"schema": "chat"}

    id: Mapped[int_pk]
    chat_name: Mapped[str]
    image: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    deleted_at: Mapped[datetime.datetime | None]


class ChatMember(Base):
    __tablename__ = "chat_member"
    __table_args__ = {"schema": "chat"}

    id: Mapped[int_pk]
    chat_id: Mapped[int] = mapped_column(ForeignKey(Chat.id, ondelete="CASCADE"))
    entity_uuid: Mapped[uuid.UUID]
    created_at: Mapped[created_at]


class Message(Base):
    __tablename__ = "message"
    __table_args__ = {"schema": "chat"}

    id: Mapped[int_pk]
    chat_id: Mapped[int] = mapped_column(ForeignKey(Chat.id, ondelete="CASCADE"))
    member_id: Mapped[int] = mapped_column(
        ForeignKey(ChatMember.id, ondelete="CASCADE")
    )
    text: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    deleted_at: Mapped[datetime.datetime | None]


class MessageImage(Base):
    __tablename__ = "message_image"
    __table_args__ = {"schema": "chat"}

    id: Mapped[int_pk]
    message_id: Mapped[int] = mapped_column(ForeignKey(Message.id, ondelete="CASCADE"))
    image_url: Mapped[str]


class MessageFile(Base):
    __tablename__ = "message_file"
    __table_args__ = {"schema": "chat"}

    id: Mapped[int_pk]
    message_id: Mapped[int] = mapped_column(ForeignKey(Message.id, ondelete="CASCADE"))
    file_url: Mapped[str]
