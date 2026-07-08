from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logger import logger
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    logger.info(f"{settings.APP_NAME} Started")
    yield
    logger.info(f"{settings.APP_NAME} Stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
InsightForge-AI Enterprise Analytics Platform

Features

• Dataset Upload
• Dataset Registry
• Profiling
• Schema Detection
• Statistics
• Correlation
• Missing Values
• Outlier Detection
• Dashboard
• Analytics
• Charts
• KPI
• Forecasting
• Machine Learning
• AutoML
• AI Copilot
• Executive Reports
""",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
async def root():
    logger.info("Root endpoint called")

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "documentation": "/docs",
        "openapi": "/openapi.json",
    }