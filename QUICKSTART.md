# ⚡ Quickstart Guide

Get up and running in under 5 minutes.

---

## 1. Prerequisites Checklist

- [ ] **Python 3.11+** installed → check with `python --version`
- [ ] **VS Code** installed → [Download](https://code.visualstudio.com/)
- [ ] **GitHub Copilot extension** installed in VS Code
- [ ] **GitHub Copilot Chat extension** installed in VS Code
- [ ] **GitHub account** with Copilot access (free for students!)

### Get GitHub Copilot Free as a Student

1. Go to [education.github.com](https://education.github.com/)
2. Click **"Get student benefits"**
3. Verify with your `.edu` email address
4. GitHub Copilot will be available in your account

---

## 2. Fork and Clone

```bash
# On GitHub, click the "Fork" button in the top-right corner
# Then clone YOUR fork:
git clone https://github.com/YOUR_USERNAME/UNC-SolHacks-2026.git
cd UNC-SolHacks-2026
```

---

## 3. Set Up Python Environment

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 4. Open in VS Code

```bash
code .
```

### Verify Copilot is Working

1. Open any `.py` file
2. Start typing a function — e.g., `def add(`
3. You should see a gray suggestion from Copilot
4. Press **Tab** to accept the suggestion

### Verify Copilot Chat is Working

1. Press **Ctrl+Shift+I** (Windows) or **Cmd+Shift+I** (macOS) to open Copilot Chat
2. Type: _"What exercises are in this repository?"_
3. Copilot should respond with information about the exercises

---

## 5. Run the Tests

```bash
# Make sure your virtual environment is active, then:
pytest -v
```

You should see some tests pass and some marked as incomplete — that's intentional! The exercises are waiting for you to complete them with Copilot.

---

## 6. Start Learning!

### Recommended Order

| Order | Exercise | What You'll Practice |
|-------|----------|---------------------|
| 1st | [01 — Autocomplete](examples/01_autocomplete/) | Basic code completion |
| 2nd | [02 — Writing Tests](examples/02_writing_tests/) | Test generation |
| 3rd | [03 — Refactoring](examples/03_refactoring/) | Code cleanup |
| 4th | [04 — Documentation](examples/04_documentation/) | Docstring generation |
| 5th | [05 — Debugging](examples/05_debugging/) | Finding and fixing bugs |
| 6th | [06 — Build an API](examples/06_build_api/) | Full API development |
| 7th | [Starter Project](starter_project/) | Build something new! |

### Tips for Each Exercise

1. **Read the README** in each exercise folder first
2. **Look for `# TODO:` comments** — place your cursor there
3. **Let Copilot suggest** — don't type the answer yourself
4. **Use Copilot Chat** if you get stuck: ask _"How do I complete this TODO?"_
5. **Try multiple suggestions** — press `Ctrl+]` to cycle through alternatives

---

## Troubleshooting

### Copilot not showing suggestions?

- Make sure the Copilot icon in the bottom-right of VS Code shows a checkmark
- Check you're signed into GitHub in VS Code
- Try restarting VS Code

### Python virtual environment issues?

```bash
# Deactivate any existing environment
deactivate

# Delete and recreate
rm -rf .venv
python -m venv .venv

# Reactivate (use the command for your OS above)
```

### `pytest` not found?

```bash
# Make sure your virtual environment is active, then:
pip install -r requirements.txt
```

---

You're all set! Head to [examples/01_autocomplete/](examples/01_autocomplete/) to begin.
