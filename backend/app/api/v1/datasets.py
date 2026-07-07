from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.dataset_repository import DatasetRepository
from app.schemas.dataset import DatasetCreate, DatasetResponse
from app.services.dataset_service import DatasetService

router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"],
)


@router.get("/", response_model=list[DatasetResponse])
def get_datasets(
    db: Session = Depends(get_db),
):
    return DatasetService(
        DatasetRepository(db)
    ).get_all()


@router.post("/", response_model=DatasetResponse)
def create_dataset(
    dataset: DatasetCreate,
    db: Session = Depends(get_db),
):
    return DatasetService(
        DatasetRepository(db)
    ).create(dataset)