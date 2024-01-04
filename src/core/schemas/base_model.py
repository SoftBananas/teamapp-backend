from pydantic import BaseModel, ConfigDict


class ConfigBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
