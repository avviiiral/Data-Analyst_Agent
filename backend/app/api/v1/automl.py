from fastapi import APIRouter, HTTPException

from app.services.dataset_registry import DatasetRegistry

router = APIRouter(
    prefix="/automl",
    tags=["AutoML"],
)


@router.post("/")
def automl(dataset_id: str):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    numeric_columns = dataset.dataframe.select_dtypes(include="number").columns.tolist()

    if len(numeric_columns) < 2:
        return {
            "dataset_id": dataset_id,
            "status": "Not enough numeric columns.",
        }

    target = numeric_columns[-1]

    features = numeric_columns[:-1]

    rows = len(dataset.dataframe)

    if rows < 500:
        algorithm = "Linear Regression / Logistic Regression"

    elif rows < 5000:
        algorithm = "Random Forest"

    elif rows < 50000:
        algorithm = "XGBoost"

    else:
        algorithm = "LightGBM"

    return {
        "dataset_id": dataset_id,
        "status": "ready",
        "recommended_algorithm": algorithm,
        "target_column": target,
        "feature_columns": features,
        "rows": rows,
        "next_step": "Train model",
    }