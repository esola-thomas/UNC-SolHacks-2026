# 🎤 Demo Script — GitHub Copilot Live Walkthrough

> Estimated time: 30–45 minutes. This script guides a presenter through a live
> demonstration of GitHub Copilot for an audience of CS students.

---

## Before You Start

### Setup Checklist

- [ ] VS Code open with this repo
- [ ] GitHub Copilot extension installed and signed in
- [ ] GitHub Copilot Chat extension installed
- [ ] Python virtual environment activated (`pip install -r requirements.txt`)
- [ ] Terminal visible at the bottom of VS Code
- [ ] Font size increased for audience visibility (**Ctrl + =** to zoom in)

### Presenter Tips

- **Pause** after each Copilot suggestion so the audience can see it
- **Narrate** what you're doing: _"Watch what happens when I type this comment..."_
- **Don't rush** — the magic is in watching Copilot think
- Use **Copilot Chat** alongside inline suggestions to show both modes

---

## Demo 1: Code Autocomplete (5 min)

**File:** `examples/01_autocomplete/autocomplete_exercise.py`

### Script

1. Open the file and show the existing `# TODO:` comments
2. Say: _"Copilot reads your comments and surrounding code to predict what you want to write."_

3. **Place your cursor** on the blank line after `# TODO: Implement a function that converts Fahrenheit to Celsius`
4. Type: `def fahrenheit_to_celsius(`
5. **Pause** — let the audience see Copilot's suggestion appear in gray
6. Say: _"Copilot suggests the full function body. Press Tab to accept."_
7. Press **Tab**

8. Move to the next TODO and repeat
9. Show that Copilot **learns from context** — later functions get better suggestions because they can reference earlier ones

### Talking Points

- Copilot uses the **file context** (imports, comments, existing functions) to make predictions
- It's not copy-pasting from the internet — it **generates** code based on patterns
- You should always **review** the suggestion before accepting

---

## Demo 2: Writing Tests (5 min)

**File:** `examples/02_writing_tests/test_calculator.py`

### Script

1. Open `calculator.py` first — show the implemented functions
2. Switch to `test_calculator.py` — show the skeleton with TODOs
3. Say: _"Copilot can generate tests because it understands what the functions do."_

4. Place cursor after `# TODO: Test that add(2, 3) returns 5`
5. Type: `assert`
6. **Pause** — Copilot should suggest the full assertion
7. Accept and move to the next test

8. **Bonus:** Open Copilot Chat and type: _"Generate edge case tests for the Calculator class"_
9. Show the chat generating a comprehensive test suite

### Talking Points

- Writing tests is one of Copilot's **strongest** use cases
- It reads the source code and **generates matching tests**
- Use Chat for generating entire test files at once

---

## Demo 3: Refactoring (5 min)

**File:** `examples/03_refactoring/refactor_me.py`

### Script

1. Open the file — show the messy, working but ugly code
2. Say: _"This code works, but it's hard to read and maintain. Let's ask Copilot to clean it up."_

3. **Select all the code** in the file
4. Open Copilot Chat (**Ctrl+Shift+I**)
5. Type: _"Refactor this code to be more Pythonic, readable, and follow best practices"_
6. Show the refactored version
7. Apply the suggestion

### Talking Points

- Copilot understands **code quality** patterns
- It can rename variables, extract functions, simplify logic
- Always **run tests** after refactoring to make sure nothing broke

---

## Demo 4: Documentation (5 min)

**File:** `examples/04_documentation/document_me.py`

### Script

1. Open the file — show functions without docstrings
2. Say: _"Good code needs docs. Let's have Copilot write them."_

3. Place cursor inside the first function, on a blank line after `def`
4. Type: `"""`
5. **Pause** — Copilot generates a full docstring
6. Accept it

7. **Use Copilot Chat:** Select a function and ask _"Generate Google-style docstring for this function"_

8. **Bonus:** Ask Copilot Chat: _"Generate a README for this module explaining all functions"_

### Talking Points

- Docstrings help **you** remember what code does 6 months from now
- Copilot generates docs in common formats (Google, NumPy, reStructuredText)
- You can also use it to generate **user-facing documentation**

---

## Demo 5: Debugging (5 min)

**File:** `examples/05_debugging/buggy_code.py`

### Script

1. Run the file: `python examples/05_debugging/buggy_code.py`
2. Show the errors
3. Say: _"Let's ask Copilot to find the bugs."_

4. Open Copilot Chat
5. Type: _"This file has bugs. Find and explain each bug, then show me the fix."_
6. Walk through each bug Copilot identifies
7. Apply the fixes

8. Run the file again to show it works

### Talking Points

- Copilot can **read error messages** and suggest fixes
- It finds **logical bugs** too, not just syntax errors
- Use `/fix` in Copilot Chat for quick fixes on selected code

---

## Demo 6: Building an API (10 min)

**File:** `examples/06_build_api/app.py`

### Script

1. Open the file — show the skeleton with TODOs
2. Say: _"We're going to build a complete REST API, and Copilot will do most of the heavy lifting."_

3. Work through the TODOs one by one:
   - Let Copilot generate the data model
   - Let Copilot generate the CRUD endpoints
   - Let Copilot generate error handling

4. Run the API: `uvicorn examples.06_build_api.app:app --reload`
5. Open the browser to `http://localhost:8000/docs` — show the auto-generated docs
6. Make a few API calls from the Swagger UI

7. **Bonus:** Ask Copilot Chat to generate tests: _"Write pytest tests for all endpoints in this API"_

### Talking Points

- Copilot works especially well with **popular frameworks** like FastAPI
- It generates boilerplate so you can focus on **business logic**
- The `/docs` endpoint is generated automatically by FastAPI

---

## Demo 7: Spec-Driven Development (5 min)

### Script

1. Open `.specify/spec.md` — show the feature specification
2. Say: _"In professional development, you write a spec before you write code."_

3. Open `.specify/plan.md` — show the implementation plan
4. Open `.specify/tasks/` — show the task breakdown

5. Say: _"SpecKit + Copilot lets you go from idea → spec → plan → tasks → code"_

6. Open Copilot Chat
7. Type: _"Read the spec in .specify/spec.md and suggest the first implementation step"_
8. Show how Copilot uses the spec to guide its suggestions

### Talking Points

- **Spec-driven development** means defining _what_ before _how_
- Copilot is more effective when it has a spec to reference
- GitHub SpecKit gives you templates to structure your thinking

---

## Wrap-Up (2 min)

### Key Takeaways

1. **Copilot is a tool, not a replacement** — you still need to understand the code
2. **Context is everything** — better comments and structure = better suggestions
3. **Review before accepting** — Copilot can be wrong
4. **Use Chat for complex tasks** — inline suggestions for simple ones
5. **Spec first, code second** — AI works better when you've thought through the problem

### Call to Action

1. Fork this repo
2. Complete the remaining exercises
3. Start the **Starter Project** — build something that interests you
4. Use the **Prompt Library** for ideas on how to talk to Copilot

---

**Happy hacking! 🚀**
