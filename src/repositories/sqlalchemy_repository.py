import uuid

from pydantic import TypeAdapter
from sqlalchemy import Column, Integer, delete, insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base
from repositories.abstract_repository import AbstractRepository
from schemas.abstract_schemas import AbstractSchemas
from src.utils.logger import logger


class BaseID(Base):
    __tablename__ = "base_id"
    id = Column(Integer, primary_key=True, index=True)


class SQLAlchemyRepository(AbstractRepository):
    model: BaseID = BaseID()
    schemas: AbstractSchemas = AbstractSchemas()

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, model: schemas.create) -> int | uuid.UUID | IntegrityError:
        try:
            model_id = await self.session.execute(
                insert(self.model).values(**model.model_dump()).returning(self.model.id)
            )
            await self.session.commit()
            return model_id
        except IntegrityError as error:
            logger.error(str(error))
            return error

    async def find_by_id(
        self, model_id: int | uuid.UUID
    ) -> schemas.read | None | Exception:
        try:
            models = await self.session.execute(
                select(self.model).filter(self.model.id == model_id)
            )
            row = models.all()
            if len(row) > 0:
                return self._get_schema(row[0][0])
            else:
                return None
        except Exception as error:
            logger.error(str(error))
            return error

    async def find_all(self) -> list[schemas.read] | None | Exception:
        try:
            models = await self.session.execute(select(self.model))
            rows = models.all()
            if len(rows) > 0:
                return [self._get_schema(row[0]) for row in rows]
            else:
                return None
        except Exception as error:
            logger.error(str(error))
            return error

    async def edit(self, model: schemas.update) -> None | IntegrityError:
        try:
            await self.session.execute(
                update(self.model)
                .values(**model.model_dump())
                .where(self.model.id == model.id)
                .returning(self.model.id)
            )
            await self.session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            return error

    async def remove(self, model_id: int | uuid.UUID) -> None | IntegrityError:
        try:
            await self.session.execute(
                delete(self.model).where(self.model.id == model_id)
            )
            await self.session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            return error

    async def remove_all(self) -> None | IntegrityError:
        try:
            await self.session.execute(delete(self.model))
            await self.session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            return error

    def _get_schema(self, model_to_convert: model) -> schemas.read:
        type_adapter = TypeAdapter(self.schemas.read)
        schema = type_adapter.validate_python(model_to_convert.get_dict())
        return schema
