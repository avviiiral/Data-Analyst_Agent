from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/")
def analytics():
    return {
        "status": "ready",
        "message": "Analytics Engine Initialized",
    }