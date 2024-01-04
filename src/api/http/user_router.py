from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.api.http.abstract_router import AbstractRouter
from src.core.database import DataBase
from src.repositories.user_repositories import UserRepository
from src.core.schemas.user.user_schemas import UserCreate, UserSchemasFabric
from src.services.user.user_service import UserService


class UserRouter(AbstractRouter):
    user_service: UserService

    def __init__(self, service: UserService):
        self.router = APIRouter(prefix="/users", tags=["users"])
        self.user_service = service

    def init_routes(self):
        self.router.add_api_route(
            path="",
            endpoint=self.add_user,
            methods=["POST"],
            status_code=200,
        )
        return self.router

    async def add_user(
        self,
        user: UserCreate,
    ) -> JSONResponse:
        result = await self.user_service.add_user(user)
        return JSONResponse(**result.model_dump())
