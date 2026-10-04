import math

def _check_numbers(*values):
    """Raise ValueError if any value is not an int/float (bools rejected)."""
    for v in values:
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise ValueError("All inputs must be numbers.")

def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y


def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
    Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y


def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    Raises:
        ValueError: If x, y or z is not a number.
    """
    _check_numbers(x, y, z)
    return x + y + z

def divide(x, y):
    """
    Divides x by y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is zero.
    """
    _check_numbers(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def power(x, y):
    """
    Raises x to the power y.
    Raises:
        ValueError: If inputs are not numbers, or x is negative and y is not a whole number.
    """
    _check_numbers(x, y)
    if x < 0 and y != int(y):
        raise ValueError("Negative base needs a whole-number exponent.")
    return x ** y


def average(*numbers):
    """
    Returns the average of one or more numbers.
    Raises:
        ValueError: If no numbers are given, or any is not a number.
    """
    if not numbers:
        raise ValueError("At least one number is required.")
    _check_numbers(*numbers)
    return sum(numbers) / len(numbers)


def modulo(x, y):
    """
    Returns the remainder of x divided by y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is zero.
    """
    _check_numbers(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot take modulo by zero.")
    return x % y


def sqrt(x):
    """
    Returns the square root of x.
    Raises:
        ValueError: If x is not a number or is negative.
    """
    _check_numbers(x)
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)