from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Project).all()

    def create(self, project: Project):
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project