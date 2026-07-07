import pandas as pd


class QuestionGenerator:
    def generate(self, dataframe: pd.DataFrame):
        questions = []

        for column in dataframe.columns:
            questions.append(f"What is the average {column}?")
            questions.append(f"What is the maximum {column}?")
            questions.append(f"What is the minimum {column}?")

        return questions