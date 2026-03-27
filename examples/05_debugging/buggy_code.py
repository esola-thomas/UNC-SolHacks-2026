"""
Exercise 05 — Debugging with Copilot
======================================
This file has 5 INTENTIONAL BUGS. Find and fix them all!

Use Copilot Chat: "Find all the bugs in this code and explain each one."
Or fix them one by one using inline Copilot suggestions.

Run: python examples/05_debugging/buggy_code.py
"""


# BUG 1: Off-by-one error
def sum_range(start: int, end: int) -> int:
    """Return the sum of all integers from start to end (inclusive)."""
    total = 0
    for i in range(start, end):  # BUG: should include 'end'
        total += i
    return total


# BUG 2: Wrong comparison operator
def find_maximum(numbers: list[int]) -> int | None:
    """Return the largest number in the list, or None if empty."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num < max_val:  # BUG: should be > not <
            max_val = num
    return max_val


# BUG 3: Missing return statement
def count_even_numbers(numbers: list[int]) -> int:
    """Return how many even numbers are in the list."""
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    # BUG: forgot to return count


# BUG 4: Type error — mixing strings and integers
def build_greeting(name: str, age: int) -> str:
    """Return a greeting string like 'Hello, Alice! You are 25 years old.'"""
    greeting = "Hello, " + name + "! You are " + age + " years old."  # BUG: age is int, not str
    return greeting


# BUG 5: Logic error — condition is inverted
def filter_passing_grades(grades: list[int]) -> list[int]:
    """Return only grades that are 60 or above (passing)."""
    passing = []
    for grade in grades:
        if grade < 60:  # BUG: should be >= 60
            passing.append(grade)
    return passing


# ---------------------------------------------------------------------------
# SELF-CHECKS — Fix all 5 bugs to see this pass
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    bugs_fixed = 0
    total_bugs = 5

    # Check Bug 1: sum_range
    try:
        assert sum_range(1, 5) == 15, f"Expected 15, got {sum_range(1, 5)}"
        print("  ✓ Bug 1 fixed: sum_range works correctly")
        bugs_fixed += 1
    except (AssertionError, Exception) as e:
        print(f"  ✗ Bug 1: sum_range — {e}")

    # Check Bug 2: find_maximum
    try:
        assert find_maximum([3, 7, 2, 9, 4]) == 9, f"Expected 9, got {find_maximum([3, 7, 2, 9, 4])}"
        assert find_maximum([]) is None
        print("  ✓ Bug 2 fixed: find_maximum works correctly")
        bugs_fixed += 1
    except (AssertionError, Exception) as e:
        print(f"  ✗ Bug 2: find_maximum — {e}")

    # Check Bug 3: count_even_numbers
    try:
        result = count_even_numbers([1, 2, 3, 4, 5, 6])
        assert result == 3, f"Expected 3, got {result}"
        print("  ✓ Bug 3 fixed: count_even_numbers works correctly")
        bugs_fixed += 1
    except (AssertionError, Exception) as e:
        print(f"  ✗ Bug 3: count_even_numbers — {e}")

    # Check Bug 4: build_greeting
    try:
        result = build_greeting("Alice", 25)
        assert result == "Hello, Alice! You are 25 years old.", f"Got: {result}"
        print("  ✓ Bug 4 fixed: build_greeting works correctly")
        bugs_fixed += 1
    except (TypeError, AssertionError, Exception) as e:
        print(f"  ✗ Bug 4: build_greeting — {e}")

    # Check Bug 5: filter_passing_grades
    try:
        result = filter_passing_grades([95, 42, 78, 55, 60, 88])
        assert result == [95, 78, 60, 88], f"Expected [95, 78, 60, 88], got {result}"
        print("  ✓ Bug 5 fixed: filter_passing_grades works correctly")
        bugs_fixed += 1
    except (AssertionError, Exception) as e:
        print(f"  ✗ Bug 5: filter_passing_grades — {e}")

    print(f"\n{'=' * 50}")
    if bugs_fixed == total_bugs:
        print(f"All {total_bugs} bugs fixed! Great debugging work!")
    else:
        print(f"Fixed {bugs_fixed}/{total_bugs} bugs. Keep going!")
