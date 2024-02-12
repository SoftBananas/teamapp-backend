from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)

from src.core.config import AuthConfig


class AuthCore:
    AUTH_BACKEND_NAME = "jwt"

    def __init__(self, config: AuthConfig):
        self.jwt_secret = config.auth_jwt_secret
        self.reset_password_token_secret = config.reset_password_token_secret
        self.verification_token_secret = config.verification_token_secret

        self.cookie_transport = CookieTransport(
            cookie_name="teamapp_auth", cookie_max_age=3600
        )
        self.auth_backend = AuthenticationBackend(
            name=self.AUTH_BACKEND_NAME,
            transport=self.cookie_transport,
            get_strategy=self.get_jwt_strategy,
        )

    def get_jwt_strategy(self) -> JWTStrategy:
        return JWTStrategy(secret=self.jwt_secret, lifetime_seconds=3600)
