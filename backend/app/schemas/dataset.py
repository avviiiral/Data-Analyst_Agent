from pydantic import BaseModel, ConfigDict


class DatasetCreate(BaseModel):
    name: str
    filename: str
    file_type: str
    project_id: int


class DatasetResponse(BaseModel):
    id: int
    name: str
    filename: str
    file_type: str
    project_id: int

    model_config = ConfigDict(from_attributes=True)