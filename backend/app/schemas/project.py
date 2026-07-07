from pydantic import BaseModel, ConfigDict


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    organization_id: int


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    organization_id: int

    model_config = ConfigDict(from_attributes=True)