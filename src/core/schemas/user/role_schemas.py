from pydantic import BaseModel

from src.core.schemas.abstract_schemas_fabric import AbstractSchemasFabric


class RoleInfo(BaseModel):
    name: str
    slug: str


class RoleCreate(RoleInfo):
    pass


class RoleUpdate(RoleInfo):
    id: int


class RoleRead(RoleInfo):
    id: int


class RoleSchemas(AbstractSchemasFabric):
    create = RoleCreate
    read = RoleUpdate
    update = RoleRead
