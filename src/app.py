from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.schemas.user.user_schemas import UserSchemasFabric
from src.services.user.user_service import UserService
from src.repositories.user_repositories import UserRepository
from src.core.database import DataBase
from src.api.http.user_router import UserRouter
from src.core.config.config import Mode, Config


class App(FastAPI):

    def __init__(self, config: Config | None, *args, **kwargs) -> None:
        super().__init__(
            *args, **kwargs, title=config.app.title, version=config.app.version
        )
        self.config = config if config else Config(Mode.DEV)
        self.database = DataBase(config.database)

        self.add_middleware(
            CORSMiddleware,
            allow_origins=self.config.origins,
            allow_credentials=True,
            allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
            allow_headers=[
                "Content-Type",
                "Set-Cookie",
                "Access-Control-Allow-Headers",
                "Access-Control-Allow-Origin",
                "Authorization",
            ],
        )
        self.include_routers()

    def include_routers(self):
        routers = self.init_routers()
        for router in routers:
            self.include_router(
                router, prefix="/api/v1"
            )

    def init_routers(self):
        routers = [
            self.init_user_router(),
        ]
        return routers

    def init_user_router(self):
        user_repository = UserRepository(self.database)
        user_service = UserService(user_repository, UserSchemasFabric)
        user_router = UserRouter(user_service)
        return user_router.init_routes()

