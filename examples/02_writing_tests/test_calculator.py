"""
Exercise 02 — Writing Tests with Copilot
==========================================
Write tests for the Calculator class. Let Copilot help you fill in each TODO.

Instructions:
  1. Read calculator.py to understand the Calculator class.
  2. Place your cursor after each TODO comment.
  3. Start typing an assertion and let Copilot complete it.
  4. Run: pytest examples/02_writing_tests/test_calculator.py -v
"""

import pytest
from examples.02_writing_tests.calculator import Calculator


# ---------------------------------------------------------------------------
# Fixture — creates a fresh Calculator for each test
# ---------------------------------------------------------------------------
@pytest.fixture
def calc():
    return Calculator()


# ---------------------------------------------------------------------------
# BASIC OPERATIONS
# ---------------------------------------------------------------------------

class TestAdd:
    def test_add_positive_numbers(self, calc):
        # TODO: Test that add(2, 3) returns 5
        pass

    def test_add_negative_numbers(self, calc):
        # TODO: Test that add(-1, -1) returns -2
        pass

    def test_add_zero(self, calc):
        # TODO: Test that adding zero doesn't change the value
        pass


class TestSubtract:
    def test_subtract_positive(self, calc):
        # TODO: Test that subtract(10, 4) returns 6
        pass

    def test_subtract_negative_result(self, calc):
        # TODO: Test subtraction that produces a negative result
        pass


class TestMultiply:
    def test_multiply_positive(self, calc):
        # TODO: Test that multiply(3, 4) returns 12
        pass

    def test_multiply_by_zero(self, calc):
        # TODO: Test that multiplying by zero returns 0
        pass


class TestDivide:
    def test_divide_evenly(self, calc):
        # TODO: Test that divide(10, 2) returns 5.0
        pass

    def test_divide_with_remainder(self, calc):
        # TODO: Test that divide(7, 2) returns 3.5
        pass

    def test_divide_by_zero_raises(self, calc):
        # TODO: Test that dividing by zero raises ValueError
        # Hint: use pytest.raises(ValueError)
        pass


# ---------------------------------------------------------------------------
# ADVANCED OPERATIONS
# ---------------------------------------------------------------------------

class TestPower:
    def test_power_basic(self, calc):
        # TODO: Test that power(2, 3) returns 8
        pass

    def test_power_of_zero(self, calc):
        # TODO: Test that any number to the power of 0 is 1
        pass


class TestSquareRoot:
    def test_square_root_perfect(self, calc):
        # TODO: Test that square_root(9) returns 3.0
        pass

    def test_square_root_negative_raises(self, calc):
        # TODO: Test that square_root of a negative number raises ValueError
        pass


# ---------------------------------------------------------------------------
# HISTORY TRACKING
# ---------------------------------------------------------------------------

class TestHistory:
    def test_history_starts_empty(self, calc):
        # TODO: Test that a new calculator has empty history
        pass

    def test_history_records_results(self, calc):
        # TODO: Perform a few operations and check the history list
        pass

    def test_clear_history(self, calc):
        # TODO: Add some results, clear history, verify it's empty
        pass

    def test_last_result(self, calc):
        # TODO: Perform operations and check last_result returns the most recent
        pass

    def test_last_result_empty(self, calc):
        # TODO: Test that last_result returns None when history is empty
        pass
