# Exercise 04 — Documentation Generation

## Goal

Learn how Copilot generates docstrings, comments, and documentation.

## Instructions

1. Open `document_me.py` — the functions have **no documentation**
2. Place your cursor inside a function, on a blank line right after `def ...(...):`
3. Type `"""` (triple quotes)
4. **Wait** — Copilot will generate a full docstring
5. Press **Tab** to accept

## Copilot Chat Methods

Try these prompts in Copilot Chat:

- _"Add Google-style docstrings to all functions in this file"_
- _"Generate a module-level docstring for this file"_
- _"Create a README explaining what this module does"_
- _"Add inline comments explaining the algorithm in the `merge_sort` function"_

## What to Notice

- Copilot infers **parameter types** and **return types** from usage
- It describes **what** the function does, not just **how**
- It includes **examples** in docstrings when the function behavior is clear

## Verify

After adding docstrings, you can check them:

```bash
python -c "import examples.04_documentation.document_me as m; help(m)"
```
