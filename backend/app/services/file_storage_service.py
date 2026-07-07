from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(exist_ok=True)


class FileStorageService:
    def save(self, file: UploadFile):
        extension = Path(file.filename).suffix

        filename = f"{uuid4().hex}{extension}"

        destination = UPLOAD_DIR / filename

        with open(destination, "wb") as buffer:
            buffer.write(file.file.read())

        return filename, str(destination)