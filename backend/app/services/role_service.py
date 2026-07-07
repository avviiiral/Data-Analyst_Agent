from app.models.role import Role
from app.repositories.role_repository import RoleRepository
from app.schemas.role import RoleCreate


class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def create(self, data: RoleCreate):
        role = Role(name=data.name)
        return self.repository.create(role)

    def get_all(self):
        return self.repository.get_all()