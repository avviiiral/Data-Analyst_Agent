from fastapi import APIRouter

router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning"],
)


@router.get("/")
def ml():
    return {
        "status": "ready",
        "engine": "scikit-learn",
    }