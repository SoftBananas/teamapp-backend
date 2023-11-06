import datetime
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base
from src.models.annotated_types import int_pk
from src.models.user import User


class Currency(Base):
    __tablename__ = "currency"
    __table_args__ = {"schema": "subscription"}

    id: Mapped[int_pk]
    name: Mapped[str]
    slug: Mapped[str]


# TODO: обсудить
class SubscriptionType(Base):
    __tablename__ = "subscription_type"
    __table_args__ = {"schema": "subscription"}

    id: Mapped[int_pk]
    name: Mapped[str]
    description: Mapped[str | None]
    max_response_count: Mapped[int]
    price: Mapped[float]
    currency_id: Mapped[int] = mapped_column(ForeignKey(Currency.id))
    slug: Mapped[str]


class Subscription(Base):
    __tablename__ = "subscription"
    __table_args__ = {"schema": "subscription"}

    id: Mapped[int_pk]
    user_uuid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(User.id, ondelete="CASCADE")
    )
    subscription_id: Mapped[int] = mapped_column(
        ForeignKey(SubscriptionType.id, ondelete="CASCADE")
    )
    date_start: Mapped[datetime.datetime | None]
    date_end: Mapped[datetime.datetime | None]

    payment: Mapped[float]
    currency_id: Mapped[int] = mapped_column(ForeignKey(Currency.id))


class Sale(Base):
    __tablename__ = "sale"
    __table_args__ = {"schema": "subscription"}

    id: Mapped[int_pk]
    code: Mapped[str | None]  # разве нот нал
    date_start: Mapped[datetime.datetime | None]
    date_end: Mapped[datetime.datetime]
    percent: Mapped[float]
    subscription_id: Mapped[int] = mapped_column(
        ForeignKey(SubscriptionType.id, ondelete="CASCADE")
    )
