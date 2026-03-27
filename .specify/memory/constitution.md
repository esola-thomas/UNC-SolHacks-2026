# Copilot Learning Lab Constitution

## Core Principles

### I. Simplicity First
Every example, exercise, and project must be understandable by a CS student with
beginner-to-intermediate Python experience. No unnecessary abstractions, no clever
tricks, no over-engineering. If a student can't read it in under 2 minutes, simplify it.

### II. Hands-On Learning
Every concept must be demonstrated through runnable code, not just documentation.
Students learn by doing — each exercise has incomplete code that they complete with
Copilot's help. All examples must be executable with `python` or `pytest`.

### III. AI-Assisted, Human-Verified
Copilot is a tool, not a replacement for understanding. Every exercise must require the
student to **review** and **verify** AI-generated code. Include self-checks (assertions)
so students can validate correctness. Never present AI output as automatically correct.

### IV. Progressive Difficulty
Exercises must follow a clear learning curve: autocomplete → testing → refactoring →
documentation → debugging → full API development. Each exercise builds confidence for
the next one.

### V. Minimal Dependencies
The repository must work with just Python 3.11+, VS Code, and GitHub Copilot. Only add
external packages (FastAPI, pytest) when they are the **focus** of an exercise. Never
require databases, Docker, or cloud services for core exercises.

## Technology Stack

- **Language**: Python 3.11+
- **Editor**: VS Code with GitHub Copilot extension
- **Testing**: pytest
- **API Framework**: FastAPI (Exercise 06 only)
- **Package Management**: pip + requirements.txt (keep it simple)

## Development Workflow

1. **Spec first**: Define what you're building in `.specify/spec.md`
2. **Plan second**: Break it down in `.specify/plan.md`
3. **Tasks third**: Create actionable tasks in `.specify/tasks/`
4. **Test alongside**: Write tests while building, not after
5. **Document as you go**: Use Copilot to generate docs during development

## Governance

This constitution guides all content in the repository. New exercises must follow
these principles. If a principle conflicts with a learning goal, the learning goal
wins — but document why you deviated.

**Version**: 1.0.0 | **Ratified**: 2026-03-27 | **Last Amended**: 2026-03-27
