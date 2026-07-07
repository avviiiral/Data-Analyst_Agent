from fastapi import APIRouter

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)


@router.get("/")
def questions():
    return {
        "status": "ready",
    }