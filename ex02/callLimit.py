from typing import Any, Callable


def callLimit(limit: int) -> Callable:
    """
    Decorator factory that returns a decorator that limits the number of
    times a function can be called.

    If the function is called more than `limit` times, it prints an error
    message.
    """
    def callLimiter(function: Callable) -> Callable:
        count = 0

        def limit_function(*args: Any, **kwargs: Any) -> Any:
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
