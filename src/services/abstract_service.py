from pydantic import TypeAdapter

from src.core.schemas.abstract_schemas_fabric import AbstractSchemasFabric
from src.repositories.abstract_repository import AbstractRepository


class AbstractService:
    schemas_fabric: type[AbstractSchemasFabric]
    create_schema: type
    read_schema: type
    update_schema: type

    def __init__(
        self,
        repository: AbstractRepository,
    ):
        self.repository = repository
        self.create_schema = self.schemas_fabric.create
        self.read_schema = self.schemas_fabric.read
        self.update_schema = self.schemas_fabric.update
