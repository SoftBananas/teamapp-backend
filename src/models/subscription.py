from datetime import datetime

from sqlalchemy import Column, String, Integer, UUID, Boolean, ForeignKey, JSON, DATETIME, DATE, Float, Text

from src.config.database import Base

import uuid

from src.models.user import User

# SUBSCRIPTION MODULE

# TODO: обсудить
class SubscriptionType(Base):
    __tablename__ = "subscription_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    max_response_count = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    currency_id = Column(Integer, nullable=False)
    slug = Column(String, nullable=False)

class Subscription(Base):
    __tablename__ = "subscription"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_uuid = Column(UUID, ForeignKey(User.uuid), nullable=False)
    subscription_id = Column(Integer, ForeignKey(SubscriptionType.id), nullable=False)
    date_start = Column(DATE, nullable=True)
    date_end = Column(DATE, nullable=False)

    payment = Column(Float, nullable=False)
    currency_id = Column(Integer, nullable=False)


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)





class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)  # разве нот нал
    date_start = Column(DATE, nullable=True)
    date_end = Column(DATE, nullable=False)
    percent = Column(Integer, nullable=False)
    subscription_id = Column(Integer, ForeignKey(SubscriptionType.id), nullable=False)
