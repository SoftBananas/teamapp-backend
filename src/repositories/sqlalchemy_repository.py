import uuid

from loguru import logger
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError

from src.database import Base, session_maker
from src.repositories.abstract_repository import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model_table: type = Base

    async def add(
        self, model: model_table
    ) -> int | uuid.UUID | IntegrityError:
        try:
            async with session_maker() as session:
                model_id = await session.execute(
                    insert(self.model_table)
                    .values(**self.get_filled_fields(model))
                    .returning(self.model_table.id)
                )
                await session.commit()
            return model_id.one()[0]
        except IntegrityError as error:
            logger.error(str(error))
            raise error

    async def find_by_id(
        self, model_id: int | uuid.UUID
    ) -> model_table | Exception:
        try:
            async with session_maker() as session:
                models = await session.execute(
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
            raise error

    async def find_all(self) -> list[model_table] | None | Exception:
        try:
            async with session_maker() as session:
                models = await session.execute(select(self.model_table))
            rows = models.all()
            if len(rows) > 0:
                return [row[0] for row in rows]
            else:
                return None
        except Exception as error:
            logger.error(str(error))
            raise error

    async def edit(self, model: model_table) -> None | IntegrityError:
        try:
            async with session_maker() as session:
                await session.execute(
                    update(self.model_table)
                    .values(**self.get_filled_fields(model))
                    .where(self.model_table.id == model.id)
                    .returning(self.model_table.id)
                )
                await session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            raise error

    async def remove(self, model_id: int | uuid.UUID) -> None | IntegrityError:
        try:
            async with session_maker() as session:
                await session.execute(
                    delete(self.model_table).where(self.model_table.id == model_id)
                )
                await session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            raise error

    async def remove_all(self) -> None | IntegrityError:
        try:
            async with session_maker() as session:
                await session.execute(delete(self.model_table))
                await session.commit()
        except IntegrityError as error:
            logger.error(str(error))
            raise error

    @staticmethod
    def get_filled_fields(model: model_table) -> dict:
        return {
            column: value
            for column, value in model.get_dict().items()
            if value is not None
        }
