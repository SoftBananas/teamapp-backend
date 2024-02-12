from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.http.routers import Routers
from src.core.config.config import Config, Mode
from src.core.database import DataBase
from src.repositories.repositories import Repositories
from src.services.services import Services
from src.utils.auth_core import AuthCore


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

        repositories = Repositories(self.database)
        auth_core = AuthCore(self.config.auth)
        services = Services(repositories, auth_core)
        routers = Routers(services)
        self.include_routers(routers.get_list())

    def include_routers(self, routers):
        for router in routers:
            self.include_router(router, prefix="/api/v1")
