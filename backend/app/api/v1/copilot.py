from fastapi import APIRouter

router = APIRouter(
    prefix="/copilot",
    tags=["AI Copilot"],
)


@router.get("/")
def copilot():
    return {
        "status": "ready",
        "model": "InsightForge AI",
    }