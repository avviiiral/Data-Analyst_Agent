from fastapi import APIRouter

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"],
)


@router.get("/")
def forecast():
    return {
        "status": "ready"
    }