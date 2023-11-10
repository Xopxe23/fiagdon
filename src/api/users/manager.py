from fastapi import APIRouter
from fastapi_users import FastAPIUsers, models

from src.api.users.register import get_register_router
from src.core.users.models import User
from src.core.users.schemas import UserCreate


class FastApiUsers(FastAPIUsers[models.UP, models.ID]):
    def get_register_router(
        self, user_schema: User, user_create_schema: UserCreate
    ) -> APIRouter:
        return get_register_router(
            self.get_user_manager, user_schema, user_create_schema
        )
