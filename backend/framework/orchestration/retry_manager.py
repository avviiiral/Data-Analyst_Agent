from __future__ import annotations

import time
from typing import Callable, Any


class RetryManager:

    def execute(
        self,
        func: Callable[..., Any],
        *args,
        retries: int = 3,
        delay: float = 0.5,
        **kwargs,
    ) -> Any:

        last_exception = None

        for attempt in range(retries):

            try:

                return func(*args, **kwargs)

            except Exception as ex:

                last_exception = ex

                if attempt < retries - 1:
                    time.sleep(delay)

        raise last_exception


retry_manager = RetryManager()