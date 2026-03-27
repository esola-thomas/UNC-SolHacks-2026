# Exercise 03 — Refactoring with Copilot

## Goal

Learn how Copilot helps clean up messy code while preserving functionality.

## Instructions

1. Open `refactor_me.py` — read the ugly-but-working code
2. Use **Copilot Chat** to refactor it:
   - Select all the code
   - Press **Ctrl+Shift+I** to open Chat
   - Ask: _"Refactor this code to be more Pythonic and readable"_
3. Review the suggestion and apply it
4. Run the self-check at the bottom to make sure nothing broke

## Refactoring Targets

The code in `refactor_me.py` has these problems on purpose:

- Single-letter variable names
- Deeply nested if/else blocks
- Magic numbers with no explanation
- Duplicated logic
- No use of Python built-ins that would simplify the code

## What to Notice

- Copilot renames variables to be **descriptive**
- It replaces manual loops with **list comprehensions** or built-ins
- It extracts **magic numbers** into named constants
- It simplifies **nested conditionals**

## Verify

```bash
python examples/03_refactoring/refactor_me.py
```

All assertions should still pass after refactoring.
