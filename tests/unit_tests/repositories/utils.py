from pydantic import BaseModel, TypeAdapter
from sqlalchemy import select

from core.models.base import Base
from tests.conftest import db


def convert_model_to_schema(self, model: Base) -> BaseModel:
    type_adapter = TypeAdapter(self.schemas.read)
    schema = type_adapter.validate_python(model.get_dict())
    return schema


async def get_existing_models(model: type[Base]) -> list[Base]:
    async with db.session_maker() as session:
        result = await session.execute(select(model))
    return [existing_model[0] for existing_model in result.all()]
