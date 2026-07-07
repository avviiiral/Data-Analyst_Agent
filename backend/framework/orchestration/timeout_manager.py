from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, TimeoutError
from typing import Callable, Any


class TimeoutManager:

    def execute(
        self,
        func: Callable[..., Any],
        *args,
        timeout: float = 5.0,
        **kwargs,
    ) -> Any:

        with ThreadPoolExecutor(max_workers=1) as executor:

            future = executor.submit(
                func,
                *args,
                **kwargs,
            )

            try:

                return future.result(
                    timeout=timeout,
                )

            except TimeoutError:

                future.cancel()

                raise TimeoutError(
                    f"Execution exceeded {timeout} seconds."
                )


timeout_manager = TimeoutManager()