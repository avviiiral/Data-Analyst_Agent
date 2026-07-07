from fastapi import APIRouter

from app.api.router import router as root_router
from app.api.v1.auth import router as auth_router
from app.api.v1.database import router as database_router
from app.api.v1.users import router as users_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(root_router)
api_router.include_router(database_router)
api_router.include_router(users_router)
api_router.include_router(auth_router)