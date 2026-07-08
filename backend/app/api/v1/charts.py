from fastapi import APIRouter, HTTPException

from app.services.ai.chart_recommender import ChartRecommender
from app.services.dataset_registry import DatasetRegistry

router = APIRouter(
    prefix="/charts",
    tags=["Charts"],
)


@router.post("/")
def recommend_charts(dataset_id: str):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    return {
        "dataset_id": dataset_id,
        "recommended_charts": ChartRecommender().recommend(dataset.dataframe),
    }