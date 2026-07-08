from fastapi import APIRouter, HTTPException

from app.services.dataset_registry import DatasetRegistry

router = APIRouter(
    prefix="/copilot",
    tags=["AI Copilot"],
)


@router.post("/")
def copilot(
    dataset_id: str,
    question: str,
):

    dataset = DatasetRegistry.get(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found.",
        )

    question_lower = question.lower()

    if "rows" in question_lower:
        answer = f"The dataset contains {len(dataset.dataframe)} rows."

    elif "columns" in question_lower:
        answer = f"The dataset contains {len(dataset.dataframe.columns)} columns."

    elif "missing" in question_lower:
        answer = (
            f"The dataset contains "
            f"{int(dataset.dataframe.isna().sum().sum())} missing values."
        )

    elif "duplicate" in question_lower:
        answer = (
            f"The dataset contains "
            f"{int(dataset.dataframe.duplicated().sum())} duplicate rows."
        )

    else:
        answer = (
            "Natural language AI Copilot "
            "will be connected to the Agent Framework in a later milestone."
        )

    return {
        "dataset_id": dataset_id,
        "question": question,
        "answer": answer,
    }