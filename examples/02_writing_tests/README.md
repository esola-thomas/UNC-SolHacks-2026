# Exercise 02 — Writing Tests with Copilot

## Goal

Learn how GitHub Copilot generates tests by reading your source code.

## Instructions

1. Open `calculator.py` — read the existing implementation
2. Open `test_calculator.py` — find the `# TODO:` comments
3. Place your cursor after each TODO
4. Start typing `assert` or `def test_` and let Copilot suggest the test
5. Run the tests to verify

## What to Notice

- Copilot reads `calculator.py` to understand **what** to test
- It generates **meaningful** test cases, not just boilerplate
- It knows common testing patterns (happy path, edge cases, error handling)

## Copilot Chat Bonus

Try this in Copilot Chat:

> "Generate comprehensive pytest tests for the Calculator class in
> examples/02_writing_tests/calculator.py. Include edge cases and error
> handling."

## Verify

```bash
pytest examples/02_writing_tests/test_calculator.py -v
```
