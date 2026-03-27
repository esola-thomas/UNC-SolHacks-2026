# Implementation Plan: Student Grade Tracker

**Branch**: `001-grade-tracker` | **Date**: 2026-03-27 | **Spec**: `.specify/spec.md`
**Input**: Feature specification from `.specify/spec.md`

## Summary

Build a simple Python module that tracks student course grades and calculates
cumulative GPA on a standard 4.0 scale. No database — in-memory with optional
JSON file persistence. Designed as a learning exercise for Copilot-assisted
development.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: None (stdlib only)
**Storage**: In-memory dictionary; optional JSON file export
**Testing**: pytest
**Target Platform**: Cross-platform CLI
**Project Type**: Library + CLI
**Performance Goals**: N/A (educational project)
**Constraints**: Must be completable in under 30 minutes with Copilot
**Scale/Scope**: Single user, up to ~50 courses

## Constitution Check

- [x] **Simplicity First**: Single module, no external dependencies
- [x] **Hands-On**: Students build it function by function with Copilot
- [x] **AI-Assisted, Human-Verified**: Self-checks validate each function
- [x] **Progressive Difficulty**: Builds on skills from exercises 01-05
- [x] **Minimal Dependencies**: Python stdlib only

## Project Structure

### Source Code

```text
starter_project/
├── main.py              # GradeTracker class and CLI
├── utils.py             # Grade scale mapping and validation helpers
├── test_main.py         # pytest tests
└── README.md            # Project description
```

## Design Decisions

1. **Single class** (`GradeTracker`) — keeps it simple
2. **Dictionary storage** — courses keyed by name
3. **Grade validation** — reject invalid grades early
4. **No persistence by default** — optional JSON save/load as stretch goal

## Complexity Tracking

No violations. This is a straightforward CRUD + calculation module.
