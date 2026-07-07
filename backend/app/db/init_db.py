from app.db.base import Base
from app.db.session import engine

from app.models.organization import Organization
from app.models.role import Role
from app.models.user import User


def init_db():
    Base.metadata.create_all(bind=engine)