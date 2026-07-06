from fastapi import APIRouter

router = APIRouter(prefix="/database", tags=["Database"])


@router.get("/status")
def database_status():
    return {
        "database": "connected",
        "engine": "SQLite",
    }