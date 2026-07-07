from __future__ import annotations

from backend.framework.base_agent import AgentResponse


class FailureRecovery:

    def recover(
        self,
        responses: list[AgentResponse],
    ) -> dict:

        successful = []
        failed = []
        retry = []

        for response in responses:

            if response.success:

                successful.append(response.agent)

            else:

                failed.append(response.agent)

                retry.append(response.agent)

        return {
            "successful": successful,
            "failed": failed,
            "retry": retry,
            "can_continue": len(failed) == 0,
        }


failure_recovery = FailureRecovery()