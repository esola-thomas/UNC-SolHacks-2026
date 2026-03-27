# 📚 Copilot Prompt Library

A curated collection of prompts that work well with GitHub Copilot and Copilot
Chat. Copy-paste these or adapt them to your needs.

---

## Table of Contents

- [Code Generation](#code-generation)
- [Testing](#testing)
- [Refactoring](#refactoring)
- [Documentation](#documentation)
- [Debugging](#debugging)
- [Architecture & Design](#architecture--design)
- [Learning & Explanation](#learning--explanation)
- [Spec-Driven Development](#spec-driven-development)

---

## Code Generation

### Generate a function from description

```
Write a Python function called {name} that {description}.
It should accept {parameters} and return {return type}.
Include type hints.
```

### Generate a class

```
Create a Python class called {ClassName} that represents {description}.
Include:
- __init__ with {attributes}
- __str__ and __repr__ methods
- {list any specific methods needed}
```

### Generate CRUD operations

```
Generate Python CRUD functions for a {entity} with fields: {fields}.
Use a dictionary as in-memory storage.
Include: create, read (single + all), update, delete.
```

### Generate a CLI tool

```
Write a Python CLI script using argparse that {description}.
Include help text for all arguments and a main() function.
```

---

## Testing

### Generate unit tests

```
Write pytest unit tests for the following function. Include:
- Happy path test cases
- Edge cases (empty input, None, boundary values)
- Error cases (invalid input that should raise exceptions)

{paste function here}
```

### Generate test fixtures

```
Create pytest fixtures for testing a {class/module} that needs:
- {setup description}
- {any mock data needed}
Use @pytest.fixture decorator.
```

### Generate parameterized tests

```
Convert these test cases into a single parameterized test using @pytest.mark.parametrize:
- Input: {input1} → Expected: {output1}
- Input: {input2} → Expected: {output2}
- Input: {input3} → Expected: {output3}
```

### Test coverage gaps

```
Look at {file} and its test file {test_file}.
What code paths are NOT covered by tests?
Generate tests for the uncovered paths.
```

---

## Refactoring

### General refactoring

```
Refactor this code to be more Pythonic and readable.
Keep the same function signatures and behavior.
Apply: descriptive names, list comprehensions where appropriate,
early returns, and remove code duplication.
```

### Extract function

```
Extract the logic in lines {X}-{Y} into a separate function
with a descriptive name. Update the original code to call it.
```

### Simplify conditionals

```
Simplify these nested if/else statements.
Consider using: early returns, guard clauses, match/case (Python 3.10+),
or dictionary dispatch.
```

### Remove code duplication

```
These {N} functions have similar logic. Refactor to eliminate duplication
by extracting shared behavior into a helper function or base class.
```

---

## Documentation

### Docstring generation

```
Add Google-style docstrings to all functions in this file.
Include: description, Args, Returns, Raises, and an Example.
```

### Module documentation

```
Write a module-level docstring for this file that explains:
- What this module does
- Key classes/functions
- Usage examples
- Dependencies
```

### README generation

```
Generate a README.md for this project that includes:
- Project title and description
- Installation instructions
- Usage examples
- API reference (if applicable)
- Contributing guidelines
```

### Inline comments

```
Add inline comments to this complex algorithm explaining
each step and why it's necessary. Focus on the "why", not the "what".
```

---

## Debugging

### Find bugs

```
This code has a bug. The expected behavior is {expected},
but the actual behavior is {actual}.
Find the bug and explain the fix.
```

### Explain an error

```
I'm getting this error:

{paste error traceback}

Explain what's causing it and how to fix it.
```

### Fix performance

```
This function is too slow for large inputs.
Profile it, identify the bottleneck, and suggest an optimized version.
Explain the time complexity improvement.
```

### Add error handling

```
Add appropriate error handling to this code.
Consider: input validation, try/except blocks, meaningful error messages,
and logging. Don't over-handle — only catch errors you can meaningfully recover from.
```

---

## Architecture & Design

### Design a module

```
Design the module structure for a {description} application.
Include: file layout, class responsibilities, key interfaces,
and how modules communicate.
```

### Design an API

```
Design a REST API for {resource}.
Include: endpoints (method + path), request/response bodies,
status codes, and error responses.
Follow RESTful conventions.
```

### Design a data model

```
Design the data model for {description}.
Include: entities, attributes, relationships, and constraints.
Use Python dataclasses or Pydantic models.
```

---

## Learning & Explanation

### Explain code

```
Explain this code line by line as if I'm a beginner.
What does each part do, and why is it written this way?
```

### Compare approaches

```
Show me 3 different ways to {task} in Python.
Compare them by: readability, performance, and when to use each.
```

### Explain a concept

```
Explain {concept} in Python with a simple example.
Assume I understand {prerequisites} but not {topic}.
```

### Code review

```
Review this code for:
- Bugs or logic errors
- Security issues
- Performance concerns
- Style and readability
- Missing edge case handling

Provide specific suggestions, not just observations.
```

---

## Spec-Driven Development

### Generate a spec from an idea

```
I want to build {description}.
Write a feature specification including:
- User stories with acceptance scenarios (Given/When/Then)
- Functional requirements
- Edge cases
- Key entities
```

### Generate a plan from a spec

```
Read the specification in {spec file}.
Generate an implementation plan including:
- Technical stack decisions
- Project structure
- Phase breakdown
- Risk assessment
```

### Generate tasks from a plan

```
Read the plan in {plan file}.
Break it down into ordered, actionable implementation tasks.
Each task should be:
- Small enough to complete in 1-2 hours
- Independently testable
- Include the exact file path to create/modify
```

### Validate spec completeness

```
Review this specification for completeness.
Identify:
- Ambiguous requirements
- Missing edge cases
- Unstated assumptions
- Potential conflicts between requirements
```

---

## Tips for Better Prompts

1. **Be specific** — "Write a function" < "Write a function called `parse_csv` that reads a CSV file and returns a list of dictionaries"
2. **Provide context** — mention the framework, language version, and coding style
3. **Include examples** — show sample input/output for clarity
4. **Specify constraints** — "must handle files up to 1GB" or "should run in O(n) time"
5. **Iterate** — start with a simple prompt, then refine based on the output

---

## Using These Prompts

### In Copilot Chat

1. Press **Ctrl+Shift+I** to open Chat
2. Paste or type any prompt from above
3. Replace the `{placeholders}` with your specifics

### As Inline Comments

Write prompts as code comments — Copilot reads them as context:

```python
# Generate a function that validates an email address using regex
# It should return True for valid emails, False otherwise
# Valid: user@example.com, first.last@domain.co.uk
# Invalid: @missing.com, user@, plain-text
def validate_email(email: str) -> bool:
    # Copilot will fill this in based on the comment above
```
