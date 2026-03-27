"""
Exercise 01 — Code Autocomplete
================================
Practice letting GitHub Copilot complete functions from comments and signatures.

Instructions:
  1. Find each TODO below.
  2. Place your cursor on the blank line after the TODO comment.
  3. Start typing the function definition.
  4. Let Copilot suggest the body — press Tab to accept.

Run this file to check your work:
  python examples/01_autocomplete/autocomplete_exercise.py
"""


# ---------------------------------------------------------------------------
# WARM-UP: Simple conversions
# ---------------------------------------------------------------------------

# TODO: Implement a function that converts Fahrenheit to Celsius
# Formula: (fahrenheit - 32) * 5 / 9


# TODO: Implement a function that converts Celsius to Fahrenheit
# Formula: celsius * 9 / 5 + 32


# TODO: Implement a function that converts miles to kilometers
# 1 mile = 1.60934 kilometers


# ---------------------------------------------------------------------------
# LEVEL UP: String utilities
# ---------------------------------------------------------------------------

# TODO: Implement a function that checks if a string is a palindrome
# A palindrome reads the same forwards and backwards (e.g., "racecar")
# Ignore case and spaces


# TODO: Implement a function that counts the number of vowels in a string
# Count both uppercase and lowercase vowels (a, e, i, o, u)


# TODO: Implement a function that reverses the words in a sentence
# Example: "hello world" -> "world hello"


# ---------------------------------------------------------------------------
# CHALLENGE: Data processing
# ---------------------------------------------------------------------------

# TODO: Implement a function that finds the two numbers in a list that add up
# to a target sum. Return them as a tuple. Return None if no pair is found.
# Example: find_pair([1, 3, 5, 7], 8) -> (1, 7) or (3, 5)


# TODO: Implement a function that flattens a nested list
# Example: flatten([[1, 2], [3, [4, 5]]]) -> [1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# SELF-CHECKS — Run this file to verify your solutions
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Running autocomplete exercise checks...\n")

    # Conversion checks
    try:
        assert abs(fahrenheit_to_celsius(32) - 0.0) < 0.01, "32°F should be 0°C"
        assert abs(fahrenheit_to_celsius(212) - 100.0) < 0.01, "212°F should be 100°C"
        print("  ✓ fahrenheit_to_celsius works!")
    except NameError:
        print("  ✗ fahrenheit_to_celsius — not yet implemented")

    try:
        assert abs(celsius_to_fahrenheit(0) - 32.0) < 0.01
        assert abs(celsius_to_fahrenheit(100) - 212.0) < 0.01
        print("  ✓ celsius_to_fahrenheit works!")
    except NameError:
        print("  ✗ celsius_to_fahrenheit — not yet implemented")

    try:
        assert abs(miles_to_kilometers(1) - 1.60934) < 0.01
        assert abs(miles_to_kilometers(0) - 0.0) < 0.01
        print("  ✓ miles_to_kilometers works!")
    except NameError:
        print("  ✗ miles_to_kilometers — not yet implemented")

    # String checks
    try:
        assert is_palindrome("racecar") is True
        assert is_palindrome("hello") is False
        assert is_palindrome("A man a plan a canal Panama") is True
        print("  ✓ is_palindrome works!")
    except NameError:
        print("  ✗ is_palindrome — not yet implemented")

    try:
        assert count_vowels("hello") == 2
        assert count_vowels("AEIOU") == 5
        assert count_vowels("xyz") == 0
        print("  ✓ count_vowels works!")
    except NameError:
        print("  ✗ count_vowels — not yet implemented")

    try:
        assert reverse_words("hello world") == "world hello"
        assert reverse_words("one") == "one"
        print("  ✓ reverse_words works!")
    except NameError:
        print("  ✗ reverse_words — not yet implemented")

    # Data processing checks
    try:
        result = find_pair([1, 3, 5, 7], 8)
        assert result is not None
        assert sum(result) == 8
        assert find_pair([1, 2, 3], 10) is None
        print("  ✓ find_pair works!")
    except NameError:
        print("  ✗ find_pair — not yet implemented")

    try:
        assert flatten([[1, 2], [3, [4, 5]]]) == [1, 2, 3, 4, 5]
        assert flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
        print("  ✓ flatten works!")
    except NameError:
        print("  ✗ flatten — not yet implemented")

    print("\nDone! Complete all TODOs to see all checks pass.")
