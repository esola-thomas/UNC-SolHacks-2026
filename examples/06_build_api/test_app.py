"""
Tests for the Task API — Exercise 06

These tests verify the API endpoints. Complete the TODOs or let Copilot
generate tests by asking: "Generate tests for the Task Manager API."

Run: pytest examples/06_build_api/test_app.py -v
"""

import pytest
from fastapi.testclient import TestClient

# NOTE: These tests will only work after you complete models.py and app.py.
# Uncomment the imports below once your API is implemented.

# from examples.06_build_api.app import app
# client = TestClient(app)


# ---------------------------------------------------------------------------
# TODO: Test the health check endpoint
# GET / should return status 200 and a message
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Test creating a task
# POST /tasks with a title should return status 201
# The response should include an id, title, description, and status
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Test getting all tasks
# After creating a task, GET /tasks should return a list containing it
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Test getting a single task
# After creating a task, GET /tasks/{id} should return that task
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Test getting a non-existent task
# GET /tasks/999 should return status 404
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Test updating a task
# PUT /tasks/{id} with new data should update and return the task
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Test deleting a task
# DELETE /tasks/{id} should return status 200
# GET /tasks/{id} after deletion should return 404
# ---------------------------------------------------------------------------
