def ft_statistics(*args, **kwargs):
    """
    Compute statistics (mean, median, quartile, std, var) from *args
    based on **kwargs instructions.

    Allowed kwargs values:
    - "mean"
    - "median"
    - "quartile"
    - "std"
    - "var"
    """
    try:
        data = [float(x) for x in args]
    except Exception:
        print("ERROR")
        return

    error_found = False

    for val in kwargs.values():

        if not args:
            print("ERROR")
            error_found = True
        else:
            if val == "mean":
                print("mean : {}".format(format_number(ft_mean(data))))
            elif val == "median":
                print("median : {}".format(format_number(ft_median(data))))
            elif val == "quartile":
                q1, q3 = ft_quartile(data)
                print("quartile : [{:.1f}, {:.1f}]".format(
                    float(q1), float(q3)))
            elif val == "std":
                print("std : {}".format(ft_std(data)))
            elif val == "var":
                print("var : {}".format(ft_var(data)))
    if error_found:
        return


def ft_mean(data):
    """Calculate mean"""
    return sum(data) / len(data)


def ft_median(data):
    """Calculate median"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2


def ft_quartile(data):
    """Calculate Q1 and Q3 using inclusive method"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    # For both odd and even, include median in both halves
    if n % 2 == 0:
        lower = sorted_data[:mid]
        upper = sorted_data[mid:]
    else:
        lower = sorted_data[:mid + 1]
        upper = sorted_data[mid:]

    return ft_median(lower), ft_median(upper)


def ft_var(data):
    """Calculate variance"""
    m = ft_mean(data)
    return sum((x - m) * (x - m) for x in data) / len(data)


def ft_std(data):
    """Calculate standard deviation"""
    return ft_var(data) ** 0.5


def format_number(value):
    """
    Format float to int if it's a whole number.
    For example: 42.0 -> 42
    """
    if value == int(value):
        return int(value)
    return value
