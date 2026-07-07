from fastapi import APIRouter

router = APIRouter(
    prefix="/automl",
    tags=["AutoML"],
)


@router.get("/")
def automl():
    return {
        "status": "ready",
    }