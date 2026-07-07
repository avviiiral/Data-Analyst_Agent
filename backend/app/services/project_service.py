from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate


class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def create(self, data: ProjectCreate):
        project = Project(
            name=data.name,
            description=data.description,
            organization_id=data.organization_id,
        )
        return self.repository.create(project)