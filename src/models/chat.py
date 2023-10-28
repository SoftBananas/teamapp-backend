from datetime import datetime

from sqlalchemy import TIMESTAMP, UUID, Column, ForeignKey, Integer, String, Text

from src.config.database import Base


class Chat(Base):
    __tablename__ = "chat"
    __table_args__ = {"schema": "chat"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_name = Column(String, nullable=False)
    image = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())


class ChatMember(Base):
    __tablename__ = "chat_member"
    __table_args__ = {"schema": "chat"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey(Chat.id), nullable=False)
    entity_uuid = Column(UUID, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())


class Message(Base):
    __tablename__ = "message"
    __table_args__ = {"schema": "chat"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey(Chat.id), nullable=False)
    member_id = Column(Integer, ForeignKey(ChatMember.id), nullable=False)
    text = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    deleted_at = Column(TIMESTAMP, nullable=True)


class MessageImage(Base):
    __tablename__ = "message_image"
    __table_args__ = {"schema": "chat"}

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey(Message.id), nullable=False)
    image_url = Column(String, nullable=False)


class MessageFile(Base):
    __tablename__ = "message_file"
    __table_args__ = {"schema": "chat"}

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey(Message.id), nullable=False)
    file_url = Column(String, nullable=False)
