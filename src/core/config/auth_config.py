class AuthConfig:
    def __init__(
        self,
        auth_jwt_secret: str,
        reset_password_token_secret: str,
        verification_token_secret: str,
    ):
        self.auth_jwt_secret = auth_jwt_secret
        self.reset_password_token_secret = reset_password_token_secret
        self.verification_token_secret = verification_token_secret
