from pydantic import BaseModel


class AbstractSchemasFabric:
    create: type[BaseModel] = BaseModel
    read: type[BaseModel] = BaseModel
    update: type[BaseModel] = BaseModel
