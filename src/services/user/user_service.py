"""
UserService отвечает за аутентификацию и регистрацию пользователя.
Всё что нужно - переопределить и дополнять методы из BaseUserManager
Использует AuthCore с информацией о стратегии (JWT) и транспортировке (Cookies),
а также UserRepository (наследник SQLAlchemyUserDatabase из FastAPIUsers)

Данный сервис используется всеми роутерами в api.http.user.auth
"""

import uuid
from typing import Optional

from fastapi import Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.core.models import User
from src.utils.auth_core import AuthCore


class UserService(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    model_table = User

    def __init__(self, repository: SQLAlchemyUserDatabase, auth_core: AuthCore):
        self.auth = auth_core
        self.reset_password_token_secret = self.auth.reset_password_token_secret
        self.verification_token_secret = self.auth.verification_token_secret
        super().__init__(repository)

    def __call__(self):
        return self

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
