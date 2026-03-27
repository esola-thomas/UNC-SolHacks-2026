# Exercise 06 — Build a REST API

## Goal

Build a complete REST API with Copilot's help using FastAPI.

## Instructions

1. Open `app.py` — a skeleton API with TODO placeholders
2. Open `models.py` — data models to complete
3. Work through the TODOs, letting Copilot suggest implementations
4. Run the API and test it

## Steps

### Step 1: Complete the Models

Open `models.py` and complete the TODO items for the Task data model.

### Step 2: Build the Endpoints

Open `app.py` and complete each `# TODO:` endpoint:

- `GET /tasks` — list all tasks
- `GET /tasks/{task_id}` — get a single task
- `POST /tasks` — create a new task
- `PUT /tasks/{task_id}` — update a task
- `DELETE /tasks/{task_id}` — delete a task

### Step 3: Run the API

```bash
uvicorn examples.06_build_api.app:app --reload
```

### Step 4: Test It

Open your browser to [http://localhost:8000/docs](http://localhost:8000/docs)
to see the auto-generated Swagger documentation. Try each endpoint!

### Step 5: Run the Tests

```bash
pytest examples/06_build_api/test_app.py -v
```

## Copilot Chat Bonus

- _"Add input validation to the POST /tasks endpoint"_
- _"Add a search/filter endpoint for tasks by status"_
- _"Generate more comprehensive tests for this API"_

## What to Notice

- Copilot is especially good with **popular frameworks** like FastAPI
- It handles **CRUD boilerplate** effortlessly
- It generates **correct HTTP status codes** and **error responses**
