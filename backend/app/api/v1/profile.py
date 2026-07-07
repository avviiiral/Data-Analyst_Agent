from fastapi import APIRouter, Depends

from app.core.current_user import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.get("/")
def profile(
    username: str = Depends(get_current_user),
):
    return {
        "username": username,
    }