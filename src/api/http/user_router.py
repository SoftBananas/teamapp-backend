import uuid

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from src.api.http.abstract_router import AbstractRouter
from src.core.schemas.user.user_schemas import UserCreate, UserUpdate
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
        self.router.add_api_route(
            path="{user_id}",
            endpoint=self.edit_user,
            methods=["PUT"],
            status_code=200,
        )
        self.router.add_api_route(
            path="",
            endpoint=self.get_all_users,
            methods=["GET"],
            status_code=200,
        )

        self.router.add_api_route(
            path="{user_id}",
            endpoint=self.get_user,
            methods=["GET"],
            status_code=200,
        )

        self.router.add_api_route(
            path="{user_id}",
            endpoint=self.get_user,
            methods=["DELETE"],
            status_code=200,
        )
        return self.router

    async def add_user(
        self,
        user: UserCreate,
    ) -> JSONResponse:
        result = await self.user_service.add_user(user)
        if isinstance(result, Exception):
            raise HTTPException(status_code=400, detail="Bad Request")
        return JSONResponse(result)

    async def edit_user(
        self,
        user_id: uuid.UUID,
        user: UserUpdate,
    ) -> JSONResponse:
        result = await self.user_service.edit_user(user_id, user)
        if isinstance(result, Exception):
            raise HTTPException(status_code=400, detail="Bad Request")
        return JSONResponse(result)

    async def get_all_users(self) -> JSONResponse:
        result = await self.user_service.get_all_users()
        if isinstance(result, Exception):
            raise HTTPException(status_code=404, detail="Not Found")
        return JSONResponse(result)

    async def get_user(self, user_id: uuid.UUID) -> JSONResponse:
        result = await self.user_service.get_user_by_id(user_id)
        if isinstance(result, Exception):
            raise HTTPException(status_code=404, detail="Not Found")
        return JSONResponse(result)

    async def delete_user(self, user_id: uuid.UUID) -> JSONResponse:
        result = await self.user_service.delete_user(user_id)
        if isinstance(result, Exception):
            raise HTTPException(status_code=404, detail="Not Found")
        return JSONResponse(result)