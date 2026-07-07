from app.models.dataset import Dataset
from app.repositories.dataset_repository import DatasetRepository
from app.schemas.dataset import DatasetCreate


class DatasetService:
    def __init__(self, repository: DatasetRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def create(self, data: DatasetCreate):
        dataset = Dataset(
            name=data.name,
            filename=data.filename,
            file_type=data.file_type,
            project_id=data.project_id,
        )

        return self.repository.create(dataset)