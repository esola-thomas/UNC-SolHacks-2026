# Tasks: Student Grade Tracker

**Input**: Design documents from `.specify/`
**Prerequisites**: plan.md (required), spec.md (required)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this belongs to (US1, US2, US3, US4)
- Exact file paths included in each task

---

## Phase 1: Setup

- [ ] T001 Create grade scale mapping in `starter_project/utils.py`
  - Define GRADE_SCALE dict: {"A": 4.0, "A-": 3.7, "B+": 3.3, ...}
  - Add `validate_grade(grade: str) -> float` function
  - Add `validate_credit_hours(hours: int) -> int` function

- [ ] T002 [P] Create `Course` dataclass in `starter_project/main.py`
  - Fields: name (str), grade (str), credit_hours (int)
  - Store grade_points as computed property

---

## Phase 2: Core Features (US1 + US2)

- [ ] T003 Implement `GradeTracker.add_course()` in `starter_project/main.py`
  - Accept name, grade, credit_hours
  - Validate inputs using utils functions
  - Raise ValueError for duplicates
  - Store in internal dict

- [ ] T004 Implement `GradeTracker.calculate_gpa()` in `starter_project/main.py`
  - Weighted average: sum(grade_points * credits) / sum(credits)
  - Return 0.0 if no courses
  - Round to 2 decimal places

- [ ] T005 [P] Write tests for add_course and calculate_gpa in `starter_project/test_main.py`
  - Test adding valid course
  - Test duplicate course raises ValueError
  - Test GPA calculation with known grades
  - Test GPA with no courses returns 0.0

**Checkpoint**: US1 + US2 complete — can add courses and calculate GPA

---

## Phase 3: Display (US3)

- [ ] T006 Implement `GradeTracker.list_courses()` in `starter_project/main.py`
  - Return list of all courses
  - Optionally format as a table string

- [ ] T007 [P] Write test for list_courses in `starter_project/test_main.py`

---

## Phase 4: Course Removal (US4)

- [ ] T008 Implement `GradeTracker.remove_course()` in `starter_project/main.py`
  - Remove by course name
  - Raise KeyError if course doesn't exist

- [ ] T009 [P] Write test for remove_course in `starter_project/test_main.py`

**Checkpoint**: All user stories complete

---

## Phase 5: Polish (Optional Stretch Goals)

- [ ] T010 [P] Add CLI interface using argparse in `starter_project/main.py`
  - Commands: add, remove, list, gpa
- [ ] T011 [P] Add JSON save/load to `starter_project/utils.py`
  - `save_to_json(tracker, filepath)`
  - `load_from_json(filepath) -> GradeTracker`
