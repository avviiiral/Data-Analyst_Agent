from sqlalchemy.orm import Session

from app.models.role import Role


class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Role).all()

    def create(self, role: Role):
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role