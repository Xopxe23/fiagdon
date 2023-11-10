from fastapi import APIRouter, Depends, status

from src.core.cottages.schemas import CottageCreate
from src.core.cottages.services import CottageService, get_cottage_service


def get_list_router() -> APIRouter:
    router = APIRouter()

    @router.get(
        "/get",
        status_code=status.HTTP_200_OK,
        response_model=list[CottageCreate]
    )
    async def get_cottages(
            cottage_service: CottageService = Depends(get_cottage_service),
    ):
        cottages = await cottage_service.get_all()
        return cottages

    return router
