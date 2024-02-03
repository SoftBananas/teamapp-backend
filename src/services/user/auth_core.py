from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)


class AuthCore:
    AUTH_BACKEND_NAME = "jwt"

    def __init__(self, jwt_secret: str):
        self.secret = jwt_secret
        self.cookie_transport = CookieTransport(
            cookie_name="teamapp_auth", cookie_max_age=3600
        )
        self.auth_backend = AuthenticationBackend(
            name=self.AUTH_BACKEND_NAME,
            transport=self.cookie_transport,
            get_strategy=self.get_jwt_strategy,
        )

    def get_jwt_strategy(self) -> JWTStrategy:
        return JWTStrategy(secret=self.secret, lifetime_seconds=3600)
