"""
Starter Project — Tests
========================
Write tests for your project here. Copilot is great at generating tests!

Instructions:
  1. Import your functions/classes from main.py or utils.py.
  2. Write a comment describing the test, then let Copilot complete it.
  3. Run: pytest starter_project/test_main.py -v

Tip: Ask Copilot Chat: "Generate tests for the functions in starter_project/main.py"
"""

import pytest
from starter_project.utils import greet


# ---------------------------------------------------------------------------
# Example test — delete this and add your own!
# ---------------------------------------------------------------------------

def test_greet_includes_name():
    """Test that greet() includes the provided name."""
    result = greet("Alice")
    assert "Alice" in result


def test_greet_includes_solhacks():
    """Test that greet() mentions SolHacks."""
    result = greet("Bob")
    assert "SolHacks" in result


# ---------------------------------------------------------------------------
# TODO: Add tests for YOUR project below.
# Let Copilot help! Write a comment like:
#   # Test that create_task returns a task with the correct title
# Then let Copilot generate the test body.
# ---------------------------------------------------------------------------
