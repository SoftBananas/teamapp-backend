from __future__ import annotations

from loguru import logger
from sqlalchemy.exc import IntegrityError

from src.services.abstract_service import AbstractService
from src.services.responses.error_responses import (
    error_response,
    integrity_error_response,
)
from src.services.responses.service_reponse import ServiceResponse
from src.services.responses.success_responses import add_success_response


class UserService(AbstractService):
    create_schema: type
    read_schema: type
    update_schema: type

    async def add_user(self, user: create_schema) -> ServiceResponse:
        try:
            user = self.repository.model_table(**user.dict())
            model_id = await self.repository.add(user)
            logger.debug(f"User created: {user}")
            print(f"\n{model_id=}\n")
            return add_success_response(str(model_id))

        except IntegrityError as error:
            logger.error(str(error))
            return integrity_error_response(str(error))

        except Exception as error:
            logger.error(str(error))
            print(str(error))
            return error_response(str(error))
