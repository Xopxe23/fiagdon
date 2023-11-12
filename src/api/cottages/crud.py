from fastapi import APIRouter, Depends, status

from src.core.cottages.exceptions import NoCottageWithThisId, NoPermission
from src.core.cottages.schemas import CottageCreate, CottageRead, CottageUpdate
from src.core.cottages.services import CottageService, get_cottage_service
from src.core.users.dependencies import current_user
from src.core.users.models import User
from src.core.utils.models import ErrorModel


def get_create_list_router() -> APIRouter:
    router = APIRouter(prefix="/cottages")

    @router.post(
        "",
        status_code=status.HTTP_201_CREATED,
        response_model=CottageCreate,
        responses={
            status.HTTP_401_UNAUTHORIZED: {
                "content": {
                    "application/json": {
                        "examples": {
                            "Unauthorized": {
                                "summary": "No token",
                                "value": {
                                    "detail": "Unauthorized"
                                }
                            }
                        }
                    }
                }
            },
        },
    )
    async def create_cottage(
            cottage_create: CottageCreate,
            cottage_service: CottageService = Depends(get_cottage_service),
            user: User = Depends(current_user)
    ):
        cottage = await cottage_service.create(user.id, cottage_create)
        return cottage

    @router.get(
        "",
        status_code=status.HTTP_200_OK,
        response_model=list[CottageRead]
    )
    async def get_cottages(
            cottage_service: CottageService = Depends(get_cottage_service),
    ):
        cottages = await cottage_service.get_all()
        return cottages

    @router.get(
        "/{cottage_id}",
        status_code=status.HTTP_200_OK,
        response_model=CottageRead,
        responses={
            status.HTTP_400_BAD_REQUEST: {
                "content": {
                    "application/json": {
                        "examples": {
                            NoCottageWithThisId.detail: {
                                "summary": "No cottage with this id",
                                "value": {
                                    "detail": NoCottageWithThisId.detail
                                }
                            }
                        }
                    }
                }
            },
        }
    )
    async def get_cottage_by_id(
            cottage_id: int,
            cottage_service: CottageService = Depends(get_cottage_service)
    ):
        cottage = await cottage_service.get_by_id(cottage_id)
        if cottage is None:
            raise NoCottageWithThisId
        return cottage

    @router.put(
        "/{cottage_id}",
        response_model=CottageCreate,
        responses={
            status.HTTP_400_BAD_REQUEST: {
                "content": {
                    "application/json": {
                        "examples": {
                            NoCottageWithThisId.detail: {
                                "summary": "No cottage with this id",
                                "value": {
                                    "detail": NoCottageWithThisId.detail
                                }
                            }
                        }
                    }
                }
            },
            status.HTTP_401_UNAUTHORIZED: {
                "content": {
                    "application/json": {
                        "examples": {
                            "Unauthorized": {
                                "summary": "No token",
                                "value": {
                                    "detail": "Unauthorized"
                                }
                            }
                        }
                    }
                }
            },
            status.HTTP_403_FORBIDDEN: {
                "content": {
                    "application/json": {
                        "examples": {
                            NoPermission.detail: {
                                "summary": "You don’t have permission to access.",
                                "value": {
                                    "detail": NoPermission.detail
                                }
                            }
                        }
                    }
                }
            }
        }
    )
    async def update_cottage(
            cottage_id: int,
            cottage_update: CottageUpdate,
            cottage_service: CottageService = Depends(get_cottage_service),
            user: User = Depends(current_user)
    ):
        current_cottage = await cottage_service.get_by_id(cottage_id)
        if current_cottage is None:
            raise NoCottageWithThisId
        elif current_cottage.owner != user.id:
            raise NoPermission
        cottage = await cottage_service.update(user.id, cottage_id, cottage_update)
        return cottage

    @router.delete(
        "/{cottage_id}",
        response_model=str,
        responses={
            status.HTTP_400_BAD_REQUEST: {
                "model": ErrorModel,
                "content": {
                    "application/json": {
                        "examples": {
                            NoCottageWithThisId.detail: {
                                "summary": "No cottage with this id",
                                "value": {
                                    "detail": NoCottageWithThisId.detail,
                                }
                            }
                        }
                    }
                }
            },
            status.HTTP_403_FORBIDDEN: {
                "model": ErrorModel,
                "content": {
                    "application/json": {
                        "examples": {
                            NoPermission.detail: {
                                "summary": "You don't have permission to access",
                                "value": {
                                    "detail": NoPermission.detail,
                                }
                            }
                        }
                    }
                }
            }
        }
    )
    async def delete_cottage(
            cottage_id: int,
            cottage_service: CottageService = Depends(get_cottage_service),
            user: User = Depends(current_user)
    ):
        current_cottage = await cottage_service.get_by_id(cottage_id)
        if current_cottage is None:
            raise NoCottageWithThisId
        elif current_cottage.owner != user.id:
            raise NoPermission
        result = await cottage_service.delete(user.id, cottage_id)
        return result

    return router
