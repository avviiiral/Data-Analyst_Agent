from sqlalchemy.orm import Session

from app.models.organization import Organization


class OrganizationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Organization).all()

    def create(self, organization: Organization):
        self.db.add(organization)
        self.db.commit()
        self.db.refresh(organization)
        return organization