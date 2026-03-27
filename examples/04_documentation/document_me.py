"""
Exercise 04 — Documentation Generation
========================================
These functions have NO documentation. Use Copilot to add docstrings.

Instructions:
  1. Place your cursor inside a function, on a new line after the "def" line.
  2. Type triple quotes: \"\"\"
  3. Let Copilot generate the docstring — press Tab to accept.
  4. Alternatively, select a function and ask Copilot Chat to document it.
"""

import math


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def matrix_multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Incompatible matrix dimensions")
    rows_a, cols_b = len(a), len(b[0])
    cols_a = len(a[0])
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result


def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


def calculate_distance(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions")
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def flatten_dict(d, parent_key="", separator="."):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, separator).items())
        else:
            items.append((new_key, v))
    return dict(items)


# ---------------------------------------------------------------------------
# Quick verification
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Module functions work correctly:")

    assert merge_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    print("  ✓ merge_sort")

    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    print("  ✓ binary_search")

    assert is_prime(17) is True
    assert is_prime(4) is False
    print("  ✓ is_prime")

    assert matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    print("  ✓ matrix_multiply")

    assert caesar_cipher("Hello", 3) == "Khoor"
    assert caesar_cipher("Khoor", 3, decrypt=True) == "Hello"
    print("  ✓ caesar_cipher")

    assert abs(calculate_distance((0, 0), (3, 4)) - 5.0) < 0.01
    print("  ✓ calculate_distance")

    assert flatten_dict({"a": {"b": 1, "c": {"d": 2}}}) == {"a.b": 1, "a.c.d": 2}
    print("  ✓ flatten_dict")

    print("\nNow add docstrings to every function using Copilot!")
