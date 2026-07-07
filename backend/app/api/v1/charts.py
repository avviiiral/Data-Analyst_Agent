from fastapi import APIRouter

router = APIRouter(
    prefix="/charts",
    tags=["Charts"],
)


@router.get("/")
def charts():
    return {
        "status": "ready"
    }