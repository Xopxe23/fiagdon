from fastapi import APIRouter

from src.api.users.manager import FastApiUsers
from src.core.users.models import User
from src.core.users.schemas import UserCreate, UserRead, UserUpdate
from src.core.users.services import get_user_manager
from src.core.users.utils import auth_backend

fastapi_users = FastApiUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="",
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="",
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="",
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users"
)
