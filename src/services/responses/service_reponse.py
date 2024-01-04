from pydantic import BaseModel


class ServiceResponse(BaseModel):
    status_code: int
    content: dict
