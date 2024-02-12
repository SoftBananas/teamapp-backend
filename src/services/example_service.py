from __future__ import annotations

import uuid

from loguru import logger
from pydantic import TypeAdapter
from sqlalchemy.exc import IntegrityError

from src.core.schemas.user.user_schemas import UserSchemasFabric
from src.services.abstract_service import AbstractService


class UserService(AbstractService):
    schemas_fabric = UserSchemasFabric
    create_schema: type
    read_schema: type
    update_schema: type

    async def add_user(
        self, user: create_schema
    ) -> uuid.UUID | IntegrityError | Exception:
        try:
            user = self.repository.model_table(**user.dict())
            model_id = await self.repository.add(user)
            logger.debug(f"User created: {user}")
            return model_id

        except IntegrityError as error:
            logger.error(str(error))
            return error

        except Exception as error:
            logger.error(str(error))
            return error

    async def edit_user(
        self, user_id: uuid.UUID, user: update_schema
    ) -> None | IntegrityError | Exception:
        try:
            user = self.repository.model_table(id=user_id, **user.dict())
            await self.repository.edit(user)
            logger.debug(f"User edited: {user}")

        except IntegrityError as error:
            logger.error(str(error))
            return error

        except Exception as error:
            logger.error(str(error))
            return error

    async def get_user_by_id(self, user_id: int) -> read_schema | Exception:
        try:
            user = await self.repository.find_by_id(user_id)
            logger.debug(f"User found: {user}")
            return TypeAdapter(self.read_schema).validate_python(user)
        except Exception as error:
            logger.error(str(error))
            return error

    async def get_all_users(self) -> list[read_schema] | Exception:
        try:
            users = await self.repository.find_all()
            logger.debug(f"Users found: {users}")
            return TypeAdapter(list[self.read_schema]).validate_python(users)
        except Exception as error:
            logger.error(str(error))
            return error

    async def delete_user(self, user_id: int | uuid.UUID) -> None | Exception:
        try:
            await self.repository.remove(user_id)
            logger.debug(f"User deleted: {user_id}")
        except Exception as error:
            logger.error(str(error))
            return error

    async def delete_all(self) -> None | Exception:
        try:
            await self.repository.remove_all()
            logger.debug(f"Users deleted: all")
        except Exception as error:
            logger.error(str(error))
            return error
