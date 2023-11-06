import uuid
from datetime import datetime

from pydantic import BaseModel

from models import Sex
from schemas.abstract_schemas import AbstractSchemas


class UserInfo(BaseModel):
    name: str
    lastname: str
    username: str
    email: str
    hashed_password: str
    role_id: int
    image: str | None = None
    location: dict | None = None
    sex: Sex | None = None
    birthday: datetime | None = None


class UserCreate(UserInfo):
    created_at: datetime | None = datetime.now()
    updated_at: datetime | None = datetime.now()


class UserUpdate(UserInfo):
    id: uuid.UUID
    updated_at: datetime | None = datetime.now()
    is_verified: bool
    is_blocked: bool


class UserRead(UserInfo):
    id: uuid.UUID
    is_verified: bool
    created_at: datetime
    deleted_at: datetime | None
    is_blocked: bool


class UserSchemas(AbstractSchemas):
    create = UserCreate
    read = UserRead
    update = UserUpdate
