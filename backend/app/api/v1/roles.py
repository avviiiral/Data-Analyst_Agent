from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.role_repository import RoleRepository
from app.schemas.role import RoleCreate, RoleResponse
from app.services.role_service import RoleService

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return RoleService(RoleRepository(db)).get_all()


@router.post("/", response_model=RoleResponse)
def create_role(
    role: RoleCreate,
    db: Session = Depends(get_db),
):
    return RoleService(RoleRepository(db)).create(role)