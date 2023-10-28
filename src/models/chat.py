from datetime import datetime

from sqlalchemy import Column, String, Integer, UUID, ForeignKey, DATETIME, Text

from src.config.database import Base


# CHAT MODULE

class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_name = Column(String, nullable=False)
    image = Column(String, nullable=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.now())


class ChatMember(Base):
    __tablename__ = "chat_member"

    chat_id = Column(Integer, ForeignKey(Chat.id), primary_key=True)
    entity_uuid = Column(UUID, primary_key=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.now())


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey(Chat.id), nullable=False)
    member_id = Column(Integer, ForeignKey(ChatMember.id), nullable=False)
    text = Column(Text, nullable=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.now())
    updated_at = Column(DATETIME, nullable=False, default=datetime.now())
    deleted_at = Column(DATETIME, nullable=True)


class MessageImage(Base):
    __tablename__ = "message_image"

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey(Message.id), nullable=False)
    image_url = Column(String, nullable=False)


class MessageFile(Base):
    __tablename__ = "message_file"

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey(Message.id), nullable=False)
    file_url = Column(String, nullable=False)

