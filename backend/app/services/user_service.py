from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, data: UserCreate):
        user = User(
            username=data.username,
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        return self.repository.create(user)