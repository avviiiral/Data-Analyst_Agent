from pydantic import BaseModel, ConfigDict


class FileAssetResponse(BaseModel):
    id: int
    original_name: str
    stored_name: str
    path: str
    dataset_id: int

    model_config = ConfigDict(from_attributes=True)