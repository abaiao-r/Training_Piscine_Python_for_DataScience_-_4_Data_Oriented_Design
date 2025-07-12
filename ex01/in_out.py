def square(x: int | float) -> int | float:
    """
    Return the square of a number.

    Example:
        square(3) -> 9
        square(1.5) -> 2.25
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Return the number raised to the power of itself.

    Example:
        pow(3) -> 27
        pow(1.5) -> 1.837...
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Return a closure that applies a function to an internal counter,
    incrementing the counter each time it's called.

    Example:
        f = outer(3, square)
        f() -> square(3)
        f() -> square(9)
        f() -> square(81)
    """
    def inner() -> float:
        nonlocal x
        result = function(x)
        x = result
        return result

    return inner
