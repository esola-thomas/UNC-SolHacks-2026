"""
Models for the Task API — Exercise 06

Complete the TODO items to define the data models used by the API.
"""

from pydantic import BaseModel, Field
from enum import Enum


# TODO: Create a TaskStatus enum with values: "todo", "in_progress", "done"


# TODO: Create a TaskCreate model (used for POST requests) with fields:
#   - title: str (required, min length 1, max length 100)
#   - description: str (optional, default "")
#   - status: TaskStatus (optional, default TaskStatus.TODO)


# TODO: Create a TaskUpdate model (used for PUT requests) with fields:
#   - title: str (optional)
#   - description: str (optional)
#   - status: TaskStatus (optional)
#   All fields should be Optional (None by default)


# TODO: Create a TaskResponse model (returned by the API) with fields:
#   - id: int
#   - title: str
#   - description: str
#   - status: TaskStatus
