from sqlalchemy.orm import Session

from app.models.dataset import Dataset


class DatasetRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Dataset).all()

    def create(self, dataset: Dataset):
        self.db.add(dataset)
        self.db.commit()
        self.db.refresh(dataset)
        return dataset