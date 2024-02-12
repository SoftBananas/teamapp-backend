import uuid
from datetime import date, datetime

from fastapi_users import schemas

from src.core.models import Sex
from src.core.schemas.abstract_schemas_fabric import AbstractSchemasFabric
from src.core.schemas.base_model import ConfigBaseModel


class BaseUserModel(ConfigBaseModel):
    name: str
    lastname: str
    username: str
    role_id: int
    image: str | None = None
    location: dict | None = None
    sex: Sex | None = None
    birthday: date | None = None


class UserRead(schemas.BaseUser[uuid.UUID], BaseUserModel):
    is_blocked: bool
    created_at: datetime
    deleted_at: datetime | None


class UserCreate(schemas.BaseUserCreate, BaseUserModel):
    created_at: datetime | None = datetime.now()
    updated_at: datetime | None = datetime.now()


class UserUpdate(schemas.BaseUserUpdate, BaseUserModel):
    updated_at: datetime | None = datetime.now()
    is_verified: bool
    is_blocked: bool


class UserSchemasFabric(AbstractSchemasFabric):
    create = UserCreate
    read = UserRead
    update = UserUpdate
