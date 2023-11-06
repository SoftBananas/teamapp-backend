import uuid

from loguru import logger
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base
from repositories.abstract_repository import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model_table: type = Base
    model: model_table = model_table()

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(
        self, model: model_table
    ) -> int | uuid.UUID | IntegrityError:
        try:
            model_id = await self.session.execute(
                insert(self.model_table)
                .values(**self.get_filled_fields(model))
                .returning(self.model_table.id)
            )
            await self.session.commit()
            return model_id
        except IntegrityError as error:
            logger.error(str(error))
            return error

    async def find_by_id(
        self, model_id: int | uuid.UUID
    ) -> model_table | Exception:
        try:
            models = await self.session.execute(
                select(self.model_table).filter(
                    self.model_table.id == model_id
                )
            )
            row = models.first()
            if row is not None:
                return row[0]
            else:
                return None
        except Exception as error:
            logger.error(str(error))
            return error

    async def find_all(self) -> list[model_table] | None | Exception:
        try:
            models = await self.session.execute(select(self.model_table))
            rows = models.all()
            if len(rows) > 0:
                return [row[0] for row in rows]
            else:
                return None
        except Exception as error:
            logger.error(str(error))
            return error

    async def edit(self, model: model_table) -> None | IntegrityError:
        try:
            await self.session.execute(
                update(self.model_table)
                .values(**self.get_filled_fields(model))
                .where(self.model_table.id == model.id)
                .returning(self.model_table.id)
            )
            await self.session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            return error

    async def remove(self, model_id: int | uuid.UUID) -> None | IntegrityError:
        try:
            await self.session.execute(
                delete(self.model_table).where(self.model_table.id == model_id)
            )
            await self.session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            return error

    async def remove_all(self) -> None | IntegrityError:
        try:
            await self.session.execute(delete(self.model_table))
            await self.session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            return error

    @staticmethod
    def get_filled_fields(model: model_table) -> dict:
        return {
            column: value
            for column, value in model.get_dict().items()
            if value is not None
        }
