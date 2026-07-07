from fastapi import APIRouter

router = APIRouter(
    prefix="/schema",
    tags=["Schema"],
)


@router.get("/")
def schema_information():
    return {
        "message": "Schema endpoint ready."
    }