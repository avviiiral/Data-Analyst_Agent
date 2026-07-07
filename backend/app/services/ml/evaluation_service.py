from sklearn.metrics import accuracy_score


class EvaluationService:
    def evaluate(
        self,
        actual,
        predicted,
    ):
        return {
            "accuracy": accuracy_score(
                actual,
                predicted,
            )
        }