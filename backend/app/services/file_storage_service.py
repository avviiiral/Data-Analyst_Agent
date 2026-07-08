from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class FileStorageService:
    def __init__(self):
        self.datasets = {}

    def save(self, file: UploadFile):
        if not file.filename:
            raise ValueError("Uploaded file has no filename.")

        extension = Path(file.filename).suffix.lower()

        filename = f"{uuid4().hex}{extension}"

        destination = UPLOAD_DIR / filename

        with open(destination, "wb") as buffer:
            buffer.write(file.file.read())

        dataset_id = str(uuid4())

        self.datasets[dataset_id] = {
            "id": dataset_id,
            "original_name": file.filename,
            "stored_name": filename,
            "path": str(destination),
        }

        return self.datasets[dataset_id]

    def get(self, dataset_id: str):
        return self.datasets.get(dataset_id)

    def list(self):
        return list(self.datasets.values())