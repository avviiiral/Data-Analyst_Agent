from fastapi import APIRouter

from app.api.router import router as root_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(root_router)