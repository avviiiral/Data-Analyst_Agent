from fastapi import APIRouter

router = APIRouter(
    prefix="/kpi",
    tags=["KPI"],
)


@router.get("/")
def kpi():
    return {
        "status": "ready"
    }