from sqlalchemy.orm import Session

from app.models.file_asset import FileAsset


class FileAssetRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, asset: FileAsset):
        self.db.add(asset)
        self.db.commit()
        self.db.refresh(asset)
        return asset

    def get_all(self):
        return self.db.query(FileAsset).all()