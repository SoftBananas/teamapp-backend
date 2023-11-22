from pydantic import BaseModel


class ConfigBaseModel(BaseModel):
    class Config:
        from_attributes = True
