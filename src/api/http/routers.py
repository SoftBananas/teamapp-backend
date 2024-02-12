from src.api.http.user import *
from src.services.services import Services


class Routers:

    def __init__(self, services: Services):
        self.auth_router = AuthRouter(services.user_service).init_routes()
        self.register_router = RegisterRouter(services.user_service).init_routes()
        self.verify_router = VerifyRouter(services.user_service).init_routes()
        self.reset_password_router = ResetPasswordRouter(
            services.user_service
        ).init_routes()
        self.user_router = UserRouter(services.user_service).init_routes()

        self.routers = [
            self.__dict__[router]
            for router in self.__dict__
            if router.endswith("_router")
        ]

    def get_list(self):
        return self.routers
