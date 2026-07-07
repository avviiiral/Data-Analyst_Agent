from fastapi import APIRouter

router = APIRouter(
    prefix="/executive",
    tags=["Executive Report"],
)


@router.get("/")
def executive():
    return {
        "status": "ready",
    }