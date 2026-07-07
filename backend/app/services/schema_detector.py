class SchemaDetector:
    def detect(self, dataframe):
        schema = []

        for column in dataframe.columns:
            schema.append(
                {
                    "column": column,
                    "dtype": str(dataframe[column].dtype),
                }
            )

        return schema