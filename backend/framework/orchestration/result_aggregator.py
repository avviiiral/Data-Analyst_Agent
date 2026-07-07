from __future__ import annotations

from backend.framework.base_agent import AgentResponse


class ResultAggregator:

    def aggregate(
        self,
        responses: list[AgentResponse],
    ) -> dict:

        successful = []
        failed = []
        data = {}

        for response in responses:

            if response.success:

                successful.append(response.agent)

            else:

                failed.append(response.agent)

            data[response.agent] = response.data

        return {
            "total": len(responses),
            "successful": successful,
            "failed": failed,
            "data": data,
        }


result_aggregator = ResultAggregator()