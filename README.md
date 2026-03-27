# 🤖 UNC SolHacks 2026 — GitHub Copilot Learning Lab

> A hands-on workshop for learning AI-assisted development with GitHub Copilot.

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Copilot](https://img.shields.io/badge/GitHub-Copilot-blueviolet.svg)](https://github.com/features/copilot)

---

## What You'll Learn

| Exercise | Skill | Time |
|----------|-------|------|
| [01 — Autocomplete](examples/01_autocomplete/) | Let Copilot finish your code | 10 min |
| [02 — Writing Tests](examples/02_writing_tests/) | Generate tests from implementations | 10 min |
| [03 — Refactoring](examples/03_refactoring/) | Clean up messy code with AI | 10 min |
| [04 — Documentation](examples/04_documentation/) | Auto-generate docstrings & docs | 10 min |
| [05 — Debugging](examples/05_debugging/) | Find and fix bugs with Copilot | 10 min |
| [06 — Build an API](examples/06_build_api/) | Scaffold a full REST API | 15 min |
| [Starter Project](starter_project/) | Build your own project from scratch | 30+ min |

## Repository Structure

```
UNC-SolHacks-2026/
├── README.md                  ← You are here
├── QUICKSTART.md              ← Setup instructions
├── DEMO_SCRIPT.md             ← Live demo walkthrough
├── requirements.txt           ← Python dependencies
├── pyproject.toml             ← Project configuration
│
├── examples/
│   ├── 01_autocomplete/       ← Code completion exercises
│   ├── 02_writing_tests/      ← Test generation exercises
│   ├── 03_refactoring/        ← Code refactoring exercises
│   ├── 04_documentation/      ← Docstring generation exercises
│   ├── 05_debugging/          ← Bug-finding exercises
│   └── 06_build_api/          ← API building exercise
│
├── prompts/                   ← Copilot prompt library
│   └── copilot_prompts.md     ← Curated prompts for common tasks
│
├── starter_project/           ← Your blank canvas to build on
│   ├── main.py
│   ├── utils.py
│   └── test_main.py
│
├── .specify/                  ← Spec-Driven Development (SpecKit)
│   ├── spec.md                ← Feature specification
│   ├── plan.md                ← Implementation plan
│   ├── memory/
│   │   └── constitution.md    ← Project principles
│   ├── templates/             ← SpecKit templates
│   └── tasks/                 ← Task breakdown
│
├── .github/                   ← GitHub Copilot agents & prompts
│   ├── agents/                ← SpecKit agent definitions
│   └── prompts/               ← SpecKit prompt definitions
│
└── .vscode/
    └── settings.json          ← VS Code configuration
```

## Prerequisites

- **Python 3.11+** — [Download](https://www.python.org/downloads/)
- **VS Code** — [Download](https://code.visualstudio.com/)
- **GitHub Copilot** — [Get access](https://github.com/features/copilot) (free for students via [GitHub Education](https://education.github.com/))

## Quick Setup

```bash
# 1. Fork this repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/UNC-SolHacks-2026.git
cd UNC-SolHacks-2026

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Open in VS Code
code .
```

See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions.

## How to Use This Repo

1. **Fork** this repository to your GitHub account
2. **Clone** your fork locally
3. **Open** in VS Code with GitHub Copilot enabled
4. **Work through** the exercises in `examples/` — each folder has its own README
5. **Experiment** with the [Prompt Library](prompts/copilot_prompts.md)
6. **Build** your own project in the `starter_project/` folder

> **Tip:** In each exercise, look for `# TODO:` comments — that's where Copilot shines. Place your cursor after the comment and let Copilot suggest code. Press `Tab` to accept.

## Spec-Driven Development

This repo includes a **spec-driven development** workflow powered by [SpecKit](https://github.com/github/spec-kit). The `.specify/` directory contains:

- **constitution.md** — Project principles and constraints
- **spec.md** — Feature specification with user stories
- **plan.md** — Implementation plan with technical details
- **tasks/** — Broken-down, actionable implementation tasks

This teaches you how real teams plan features _before_ writing code, and how Copilot helps at every stage.

## How to Fork and Build Your Own Project

Ready to go beyond the exercises? Here's how to turn this into your own project:

### Step 1: Fork & Rename
1. Click **Fork** on GitHub
2. Rename the repo to your project name (Settings → General)

### Step 2: Clear the Exercises
```bash
# Remove the example exercises (keep the structure you want)
rm -rf examples/

# Keep the starter project as your base
mv starter_project/ src/
```

### Step 3: Define Your Spec
1. Edit `.specify/memory/constitution.md` with your project's principles
2. Create `.specify/spec.md` describing your feature
3. Use Copilot Chat: _"Read the spec and generate a plan"_

### Step 4: Build with Copilot
1. Start with your spec and plan
2. Ask Copilot to generate code from your spec
3. Write tests first, then let Copilot implement
4. Iterate: spec → plan → tasks → code → test → refine

### Step 5: Ship It
1. Add a proper README for your project
2. Set up CI/CD (GitHub Actions)
3. Deploy and share!

## Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific exercise
pytest examples/02_writing_tests/

# Run with verbose output
pytest -v
```

## Contributing

This is a learning resource! If you find issues or want to add exercises:

1. Fork the repo
2. Create a feature branch
3. Submit a Pull Request

## License

[MIT](LICENSE) — use this freely for your own workshops and courses.

---

**Built with ❤️ for UNC SolHacks 2026**