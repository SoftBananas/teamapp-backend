from pydantic import BaseModel

from schemas.abstract_schemas import AbstractSchemas


class RoleInfo(BaseModel):
    name: str
    slug: str


class RoleCreate(RoleInfo):
    pass


class RoleUpdate(RoleInfo):
    id: int


class RoleRead(RoleInfo):
    id: int


class RoleSchemas(AbstractSchemas):
    create = RoleCreate
    read = RoleUpdate
    update = RoleRead
