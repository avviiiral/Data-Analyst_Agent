from fastapi import APIRouter

router = APIRouter(
    prefix="/system",
    tags=["System"],
)


@router.get("/info")
async def system_info():
    return {
        "application": "InsightForge-AI",
        "version": "1.0.0",
        "environment": "Development",
    }