from fastapi import APIRouter

router = APIRouter(
    prefix="/outliers",
    tags=["Outliers"],
)


@router.get("/")
def outliers():
    return {
        "status": "ready"
    }