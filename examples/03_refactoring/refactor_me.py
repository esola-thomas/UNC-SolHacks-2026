"""
Exercise 03 — Refactoring with Copilot
========================================
This code WORKS but is intentionally messy. Your job is to refactor it with
Copilot's help while keeping all the self-checks passing.

How to refactor:
  1. Select all code in this file.
  2. Open Copilot Chat (Ctrl+Shift+I).
  3. Ask: "Refactor this code to be more Pythonic, readable, and follow best
     practices. Keep the same function signatures and behavior."
  4. Review the suggestion and apply it.
  5. Run the self-checks to make sure nothing broke.

Run: python examples/03_refactoring/refactor_me.py
"""


# --- MESSY FUNCTION 1: Grade calculator ---

def g(s):
    # calculates letter grade from numeric score
    if s >= 90:
        if s >= 97:
            r = "A+"
        elif s >= 93:
            r = "A"
        else:
            r = "A-"
    elif s >= 80:
        if s >= 87:
            r = "B+"
        elif s >= 83:
            r = "B"
        else:
            r = "B-"
    elif s >= 70:
        if s >= 77:
            r = "C+"
        elif s >= 73:
            r = "C"
        else:
            r = "C-"
    elif s >= 60:
        r = "D"
    else:
        r = "F"
    return r


# --- MESSY FUNCTION 2: Statistics ---

def st(n):
    # does some stats on a list of numbers
    if len(n) == 0:
        return None
    s = 0
    for i in range(len(n)):
        s = s + n[i]
    m = s / len(n)
    n2 = []
    for i in range(len(n)):
        n2.append(n[i])
    for i in range(len(n2)):
        for j in range(i + 1, len(n2)):
            if n2[i] > n2[j]:
                t = n2[i]
                n2[i] = n2[j]
                n2[j] = t
    if len(n2) % 2 == 0:
        md = (n2[len(n2) // 2 - 1] + n2[len(n2) // 2]) / 2
    else:
        md = n2[len(n2) // 2]
    mn = n2[0]
    mx = n2[len(n2) - 1]
    return {"mean": m, "median": md, "min": mn, "max": mx}


# --- MESSY FUNCTION 3: FizzBuzz ---

def fb(n):
    # fizzbuzz but ugly
    r = []
    x = 1
    while x <= n:
        if x % 3 == 0 and x % 5 == 0:
            r.append("FizzBuzz")
        elif x % 3 == 0:
            r.append("Fizz")
        elif x % 5 == 0:
            r.append("Buzz")
        else:
            r.append(str(x))
        x = x + 1
    return r


# --- MESSY FUNCTION 4: Word frequency counter ---

def wf(t):
    # counts words
    w = t.lower().split()
    d = {}
    for i in range(len(w)):
        x = w[i]
        # remove punctuation
        x2 = ""
        for c in x:
            if c >= "a" and c <= "z":
                x2 = x2 + c
        if x2 != "":
            if x2 in d:
                d[x2] = d[x2] + 1
            else:
                d[x2] = 1
    # sort by frequency
    r = []
    for k in d:
        r.append((k, d[k]))
    for i in range(len(r)):
        for j in range(i + 1, len(r)):
            if r[i][1] < r[j][1]:
                t2 = r[i]
                r[i] = r[j]
                r[j] = t2
    return r


# ---------------------------------------------------------------------------
# SELF-CHECKS — Run this file to verify refactoring didn't break anything
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Running refactoring self-checks...\n")

    # Grade calculator checks
    assert g(98) == "A+"
    assert g(95) == "A"
    assert g(91) == "A-"
    assert g(88) == "B+"
    assert g(85) == "B"
    assert g(81) == "B-"
    assert g(78) == "C+"
    assert g(74) == "C"
    assert g(71) == "C-"
    assert g(65) == "D"
    assert g(55) == "F"
    print("  ✓ Grade calculator works!")

    # Statistics checks
    result = st([4, 1, 7, 3, 9])
    assert result["mean"] == 4.8
    assert result["median"] == 4
    assert result["min"] == 1
    assert result["max"] == 9
    assert st([]) is None
    print("  ✓ Statistics works!")

    # FizzBuzz checks
    result = fb(15)
    assert result[0] == "1"
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"
    assert len(result) == 15
    print("  ✓ FizzBuzz works!")

    # Word frequency checks
    result = wf("the cat sat on the mat the cat")
    assert result[0] == ("the", 3)
    assert result[1] == ("cat", 2)
    print("  ✓ Word frequency works!")

    print("\n✅ All self-checks passed! Your refactoring didn't break anything.")
