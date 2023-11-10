from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, models

from src.config import settings
from src.core.users.exceptions import PhoneNumberAlreadyExists
from src.core.users.models import User
from src.core.users.repositories import UserRepository, get_user_db
from src.core.users.schemas import UserCreate

SECRET = settings.SECRET


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    user_db = UserRepository

    async def create(
            self,
            user_create: UserCreate,
            safe: bool = False,
            request: Optional[Request] = None,
    ) -> models.UP:
        existing_user = await self.user_db.get_by_phone_number(user_create.phone_number)
        if existing_user is not None:
            raise PhoneNumberAlreadyExists
        return await super().create(user_create, safe, request)

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(
            f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
