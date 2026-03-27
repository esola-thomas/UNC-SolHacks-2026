# Feature Specification: Student Grade Tracker

**Feature Branch**: `001-grade-tracker`
**Created**: 2026-03-27
**Status**: Draft
**Input**: User description: "Build a simple student grade tracker that calculates GPA"

## User Scenarios & Testing

### User Story 1 — Add a Course Grade (Priority: P1)

As a student, I want to add a course with its grade so that it's tracked for GPA
calculation.

**Why this priority**: This is the core feature — without adding grades, nothing
else works.

**Independent Test**: Can be tested by adding a course and verifying it appears in
the course list.

**Acceptance Scenarios**:

1. **Given** an empty grade tracker, **When** I add "CS 101" with grade "A",
   **Then** the tracker contains one course with grade "A"
2. **Given** a tracker with courses, **When** I add a duplicate course name,
   **Then** the system raises an error

---

### User Story 2 — Calculate GPA (Priority: P1)

As a student, I want to see my cumulative GPA so that I know my academic standing.

**Why this priority**: GPA calculation is the primary value the tool provides.

**Independent Test**: Add several courses with known grades, verify the GPA matches
the expected calculation.

**Acceptance Scenarios**:

1. **Given** courses with grades A, B, C (3 credits each), **When** I request GPA,
   **Then** the system returns 3.0
2. **Given** no courses, **When** I request GPA, **Then** the system returns 0.0

---

### User Story 3 — View All Courses (Priority: P2)

As a student, I want to see a list of all my courses and grades so I can review my
record.

**Why this priority**: Display is important but secondary to data entry and calculation.

**Independent Test**: Add courses, call list function, verify all courses appear.

**Acceptance Scenarios**:

1. **Given** 3 courses added, **When** I list courses, **Then** I see all 3 with
   grades and credit hours

---

### User Story 4 — Remove a Course (Priority: P3)

As a student, I want to remove a course if I drop it, so my GPA is accurate.

**Why this priority**: Nice to have; students can work around this by recreating
the tracker.

**Independent Test**: Add a course, remove it, verify GPA updates.

**Acceptance Scenarios**:

1. **Given** a course "CS 101" exists, **When** I remove "CS 101", **Then** it no
   longer appears in the list and GPA recalculates

### Edge Cases

- What happens when all courses are removed? (GPA should return 0.0)
- What happens with an invalid grade letter? (Should raise ValueError)
- What happens with 0 credit hours? (Should raise ValueError)

## Requirements

### Functional Requirements

- **FR-001**: System MUST allow adding a course with name, grade (A-F), and credit hours
- **FR-002**: System MUST calculate GPA using standard 4.0 scale
- **FR-003**: System MUST list all courses with their grades and credit hours
- **FR-004**: System MUST allow removing a course by name
- **FR-005**: System MUST validate grade inputs (A, A-, B+, B, B-, C+, C, C-, D, F)
- **FR-006**: System MUST validate credit hours are positive integers

### Key Entities

- **Course**: name (str), grade (str), credit_hours (int)
- **GradeTracker**: collection of courses, GPA calculation logic

### Grade Scale

| Grade | Points |
|-------|--------|
| A     | 4.0    |
| A-    | 3.7    |
| B+    | 3.3    |
| B     | 3.0    |
| B-    | 2.7    |
| C+    | 2.3    |
| C     | 2.0    |
| C-    | 1.7    |
| D     | 1.0    |
| F     | 0.0    |
