# Exercise 05 — Debugging with Copilot

## Goal

Learn how Copilot finds and fixes bugs in code.

## Instructions

1. Open `buggy_code.py` — there are **5 intentional bugs**
2. First, try running the file: `python examples/05_debugging/buggy_code.py`
3. See the errors? Now use Copilot to find and fix them.

### Method 1: Copilot Chat

1. Select the code in the file
2. Open Copilot Chat (**Ctrl+Shift+I**)
3. Ask: _"Find all the bugs in this code and explain each one"_
4. Apply the fixes Copilot suggests

### Method 2: Inline Fix

1. When you see a squiggly underline (error), hover over it
2. Click the **Copilot lightbulb** or press **Ctrl+.**
3. Select Copilot's suggested fix

## Bug Hints

The 5 bugs are in these categories:

1. **Off-by-one error** — a loop boundary is wrong
2. **Wrong operator** — a comparison goes the wrong direction
3. **Missing return** — a function doesn't return its result
4. **Type error** — mixing strings and numbers
5. **Logic error** — a condition is inverted

## Verify

```bash
python examples/05_debugging/buggy_code.py
```

After fixing all 5 bugs, you should see:
```
All 5 bugs fixed! Great debugging work!
```
