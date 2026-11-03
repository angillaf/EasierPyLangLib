"""
Useful formulas and small helpers to make Python easier.
"""


def fib(x: int):
    """
    Return the x-th Fibonacci number.

    Example:
        fib(7) -> 13
    """
    if x < 0:
        raise ValueError("x must be greater than or equal to 0")

    a, b = 0, 1
    for _ in range(x):
        a, b = b, a + b
    return a


def BMI(w: float, h: float):
    """
    Calculate the body mass index (BMI).

    BMI = weight / height^2
    """
    if h <= 0:
        raise ValueError("Height must be greater than 0")
    return w / h ** 2


def factorial(n: int):
    """Return n! for non-negative integers."""
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def average(*values):
    """Return the average of the provided numbers."""
    if not values:
        raise ValueError("At least one value is required")
    return sum(values) / len(values)


def is_even(value: int):
    """Return True if value is even."""
    return value % 2 == 0


def gcd(a: int, b: int):
    """Return the greatest common divisor of a and b."""
    if a == 0 and b == 0:
        return 0

    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def clamp(value, minimum, maximum):
    """Clamp a value to the range [minimum, maximum]."""
    if minimum > maximum:
        minimum, maximum = maximum, minimum
    return max(minimum, min(value, maximum))
