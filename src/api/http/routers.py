from src.services.services import Services
from src.api.http.user_router import UserRouter


class Routers:
    routers = []

    def __init__(self, services: Services):
        self.user_router = UserRouter(services.user_service).init_routes()

    def get_list(self):
        return [
            self.user_router,
        ]
