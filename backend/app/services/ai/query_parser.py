class QueryParser:
    def parse(self, query: str):
        query = query.lower()

        if "average" in query:
            return "average"

        if "sum" in query:
            return "sum"

        if "count" in query:
            return "count"

        if "maximum" in query or "max" in query:
            return "max"

        if "minimum" in query or "min" in query:
            return "min"

        return "unknown"