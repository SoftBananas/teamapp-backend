from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.database import DataBase
from src.api.http.user_router import UserRouter
from src.core.config.config import Mode, Config


class App:
    ROUTERS_V1 = [UserRouter]

    def __init__(self, config: Config | None):
        self.config = config if config else Config(Mode.DEV)
        self.database = DataBase(config)
        self.app = FastAPI(title="TEAMAPP", version="0.0.1")

    def init_app(self) -> FastAPI:
        self.app.add_middleware(
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
        for router in self.ROUTERS_V1:
            self.app.include_router(
                router(self.database).init_routes(), prefix="/api/v1"
            )

        return self.app