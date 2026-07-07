from app.models.organization import Organization
from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization import OrganizationCreate


class OrganizationService:
    def __init__(self, repository: OrganizationRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def create(self, data: OrganizationCreate):
        organization = Organization(
            name=data.name,
            description=data.description,
        )
        return self.repository.create(organization)