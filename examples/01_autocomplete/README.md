# Exercise 01 — Code Autocomplete

## Goal

Learn how GitHub Copilot suggests code completions based on comments, function
names, and surrounding context.

## Instructions

1. Open `autocomplete_exercise.py`
2. Find each `# TODO:` comment
3. Place your cursor on the **blank line** below the comment
4. Start typing the function signature (e.g., `def fahrenheit_to_celsius(`)
5. **Wait** — Copilot will suggest the rest in gray text
6. Press **Tab** to accept the suggestion
7. If the suggestion isn't right, press **Esc** and try again, or press
   **Ctrl+]** to see alternative suggestions

## What to Notice

- Copilot reads your **comments** to understand intent
- Copilot uses **nearby functions** as patterns
- The more context you provide, the better the suggestions
- Variable names and type hints improve suggestion quality

## Challenge

After completing all TODOs, try adding your own function at the bottom of the
file. Write only a descriptive comment and see if Copilot can generate the
full function from just the comment.

## Verify

```bash
python examples/01_autocomplete/autocomplete_exercise.py
```

All assertions should pass with no errors.
