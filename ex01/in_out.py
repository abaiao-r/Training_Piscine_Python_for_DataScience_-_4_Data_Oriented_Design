def square(x: int | float) -> int | float:
    """
    Returns the square of the argument x.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Returns the exponentiation of x by itself (x ** x).
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a callable object that, when called, returns the result of
    applying 'function' to x raised to the power of the number of times
    the object has been called.
    """
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        return function(x ** count)
    return inner
