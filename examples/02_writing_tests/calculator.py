"""
Calculator module — source code for Exercise 02.

This is a fully implemented calculator. Your job in test_calculator.py is to
write tests that verify every method works correctly.
"""


class Calculator:
    """A simple calculator that tracks a running history of results."""

    def __init__(self):
        self.history: list[float] = []

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        result = a + b
        self.history.append(result)
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a and b."""
        result = a - b
        self.history.append(result)
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        result = a * b
        self.history.append(result)
        return result

    def divide(self, a: float, b: float) -> float:
        """Return the quotient of a and b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(result)
        return result

    def power(self, base: float, exponent: float) -> float:
        """Return base raised to the power of exponent."""
        result = base ** exponent
        self.history.append(result)
        return result

    def square_root(self, n: float) -> float:
        """Return the square root of n. Raises ValueError if n is negative."""
        if n < 0:
            raise ValueError("Cannot take square root of a negative number")
        result = n ** 0.5
        self.history.append(result)
        return result

    def get_history(self) -> list[float]:
        """Return the list of all past results."""
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()

    def last_result(self) -> float | None:
        """Return the most recent result, or None if history is empty."""
        return self.history[-1] if self.history else None
