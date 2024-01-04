from src.core.schemas.abstract_schemas_fabric import AbstractSchemasFabric
from src.repositories.abstract_repository import AbstractRepository


class AbstractService:
    create_schema: type
    read_schema: type
    update_schema: type

    def __init__(
        self,
        repository: AbstractRepository,
        schemas_fabric: type[AbstractSchemasFabric],
    ):
        self.repository = repository

        self.create_schema = schemas_fabric.create
        self.read_schema = schemas_fabric.read
        self.update_schema = schemas_fabric.update
