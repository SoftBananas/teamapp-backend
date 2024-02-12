import uuid

from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from src.api.http.abstract_router import AbstractRouter
from src.core.models import User
from src.services.user.user_service import UserService


class AuthRouter(AbstractRouter):

    def __init__(self, service: UserService):
        self.service = service
        self.fastapi_users = FastAPIUsers[User, uuid.UUID](
            self.service,
            [service.auth.auth_backend],
        )
        self.fastapi_users_router = self.fastapi_users.get_auth_router(
            service.auth.auth_backend
        )

        self.router = APIRouter(prefix="/auth/jwt", tags=["auth"])

    def init_routes(self):
        for route in self.fastapi_users_router.routes:
            self.router.add_api_route(
                path=route.path,
                methods=route.methods,
                endpoint=route.endpoint,
                status_code=route.status_code,
            )
        return self.router
