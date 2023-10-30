from abc import ABC

from pydantic import BaseModel


class AbstractSchemas(ABC):
    create: type(BaseModel) = BaseModel
    read: type(BaseModel) = BaseModel
    update: type(BaseModel) = BaseModel
