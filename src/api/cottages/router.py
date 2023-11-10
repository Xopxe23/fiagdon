from fastapi import APIRouter

from src.api.cottages.create import get_create_router
from src.api.cottages.list import get_list_router

router = APIRouter(prefix="/cottages", tags=["Cottages"])

router.include_router(get_create_router())
router.include_router(get_list_router())
