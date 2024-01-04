
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from src.schemas.user.user_schemas import UserCreate
from src.services.user.user_service import UserService
from src.api.dependencies import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(
    user: UserCreate,
    users_service: Annotated[UserService, Depends(user_service)],
) -> JSONResponse:
    result = await users_service.add_user(user)
    return JSONResponse(**result.model_dump())
