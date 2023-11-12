from fastapi import APIRouter

from src.api.cottages.crud import get_create_list_router

router = APIRouter(prefix="", tags=["Cottages"])

router.include_router(get_create_list_router())
