from fastapi import APIRouter

from app.api.router import router as root_router
from app.api.v1.auth import router as auth_router
from app.api.v1.database import router as database_router
from app.api.v1.profile import router as profile_router
from app.api.v1.roles import router as roles_router
from app.api.v1.system import router as system_router
from app.api.v1.users import router as users_router
from app.api.v1.organizations import router as organizations_router
from app.api.v1.projects import router as projects_router
from app.api.v1.datasets import router as datasets_router
from app.api.v1.upload import router as upload_router
from app.api.v1.profiler import router as profiler_router
from app.api.v1.schema import router as schema_router
from app.api.v1.analytics import router as analytics_router
from app.api.v1.charts import router as charts_router
from app.api.v1.reports import router as reports_router
from app.api.v1.forecast import router as forecast_router
from app.api.v1.kpi import router as kpi_router
from app.api.v1.outliers import router as outliers_router
from app.api.v1.automl import router as automl_router
from app.api.v1.ml import router as ml_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(ml_router)
api_router.include_router(automl_router)
api_router.include_router(forecast_router)
api_router.include_router(kpi_router)
api_router.include_router(outliers_router)
api_router.include_router(charts_router)
api_router.include_router(reports_router)
api_router.include_router(analytics_router)
api_router.include_router(schema_router)
api_router.include_router(profiler_router)
api_router.include_router(datasets_router)
api_router.include_router(root_router)
api_router.include_router(database_router)
api_router.include_router(users_router)
api_router.include_router(auth_router)
api_router.include_router(profile_router)
api_router.include_router(system_router)
api_router.include_router(roles_router)
api_router.include_router(organizations_router)
api_router.include_router(projects_router)
api_router.include_router(upload_router)