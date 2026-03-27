"""
Task API — Exercise 06
=======================
Build a complete REST API for managing tasks. Complete each TODO with Copilot.

Run: uvicorn examples.06_build_api.app:app --reload
Docs: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException

# TODO: Import the models you defined in models.py
# from examples.06_build_api.models import TaskStatus, TaskCreate, TaskUpdate, TaskResponse

app = FastAPI(
    title="Task Manager API",
    description="A simple task management API — built with GitHub Copilot!",
    version="1.0.0",
)

# In-memory storage (no database needed for this exercise)
tasks_db: dict[int, dict] = {}
next_id: int = 1


@app.get("/")
def root():
    """Health check endpoint."""
    return {"message": "Task Manager API is running!", "docs": "/docs"}


# ---------------------------------------------------------------------------
# TODO: Implement GET /tasks
# Return a list of all tasks.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Implement GET /tasks/{task_id}
# Return a single task by ID.
# Raise HTTPException(status_code=404) if the task doesn't exist.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Implement POST /tasks
# Create a new task from a TaskCreate model.
# Assign it an auto-incrementing ID.
# Return the created task with status code 201.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Implement PUT /tasks/{task_id}
# Update an existing task. Only update fields that are provided (not None).
# Raise HTTPException(status_code=404) if the task doesn't exist.
# Return the updated task.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Implement DELETE /tasks/{task_id}
# Delete a task by ID.
# Raise HTTPException(status_code=404) if the task doesn't exist.
# Return a confirmation message.
# ---------------------------------------------------------------------------
