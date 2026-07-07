from fastapi import APIRouter, File, UploadFile

from app.services.file_storage_service import FileStorageService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
def upload_file(
    file: UploadFile = File(...),
):
    storage = FileStorageService()

    filename, path = storage.save(file)

    return {
        "filename": filename,
        "path": path,
    }