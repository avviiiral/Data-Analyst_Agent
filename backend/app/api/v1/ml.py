from fastapi import APIRouter, HTTPException

from app.services.dataset_registry import DatasetRegistry

router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning"],
)


@router.post("/")
def run_ml(dataset_id: str):

    dataframe = DatasetRegistry.get(dataset_id)

    if dataframe is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    numeric_columns = dataframe.select_dtypes(include="number").columns.tolist()

    if len(numeric_columns) < 2:
        return {
            "dataset_id": dataset_id,
            "status": "Not enough numeric columns to train a model."
        }

    target = numeric_columns[-1]

    features = numeric_columns[:-1]

    return {
        "dataset_id": dataset_id,
        "status": "ready",
        "target_column": target,
        "feature_columns": features,
        "rows": len(dataframe),
        "algorithm": "Auto Detect (coming next)",
        "message": "Dataset is ready for ML training."
    }