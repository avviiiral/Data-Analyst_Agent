from app.core.jwt import create_access_token
from app.core.security import verify_password
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def login(self, username: str, password: str):
        user = self.repository.get_by_username(username)

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return create_access_token(user.username)