from fastapi import APIRouter, Depends, status

from src.core.cottages.schemas import CottageCreate
from src.core.cottages.services import CottageService, get_cottage_service
from src.core.users.dependencies import current_user
from src.core.users.models import User


def get_create_router() -> APIRouter:
    router = APIRouter()

    @router.post(
        "/create",
        status_code=status.HTTP_201_CREATED,
        response_model=CottageCreate,
        responses={
            status.HTTP_401_UNAUTHORIZED: {
                "description": "Missing token or inactive user.",
            },
        },
    )
    async def create_cottage(
            cottage_create: CottageCreate,
            cottage_service: CottageService = Depends(get_cottage_service),
            user: User = Depends(current_user)
    ):
        user_id = user.id
        cottage = await cottage_service.create(user_id, cottage_create)
        return cottage

    return router
