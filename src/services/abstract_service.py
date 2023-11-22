from src.repositories.abstract_repository import AbstractRepository
from src.schemas.abstract_schemas_fabric import AbstractSchemasFabric


class AbstractService:
    create_schema: type
    read_schema: type
    update_schema: type

    def __init__(
        self,
        repository: type[AbstractRepository],
        schemas_fabric: type[AbstractSchemasFabric],
    ):
        self.repository: AbstractRepository = repository()

        self.create_schema = schemas_fabric.create
        self.read_schema = schemas_fabric.read
        self.update_schema = schemas_fabric.update
