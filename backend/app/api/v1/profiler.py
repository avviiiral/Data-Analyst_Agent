from fastapi import APIRouter

router = APIRouter(
    prefix="/profiler",
    tags=["Profiler"],
)


@router.get("/")
def profiler():
    return {
        "message": "Profiler endpoint ready."
    }