from fastapi import APIRouter
from app.models import TaskCreate, TaskUpdate
import app.storage as storage

router = APIRouter(tags=["Tasks"])

NOT_FOUND = {404: {"description": "Task not found"}}


@router.get(
    "/tasks",
    summary="List all tasks",
    response_description="All tasks, ordered by ID",
)
def get_tasks():
    """Return every task stored in the database."""
    return {"tasks": storage.list_tasks()}


@router.post(
    "/tasks",
    summary="Create a task",
    response_description="The newly created task",
)
def create_task(task: TaskCreate):
    """Create a new task. `completed` defaults to `false` if omitted."""
    new_task = storage.create_task(task)
    return {"message": "Task created successfully", "task": new_task}


@router.put(
    "/tasks/{task_id}",
    summary="Update a task",
    response_description="The updated task",
    responses=NOT_FOUND,
)
def update_task(task_id: int, task_update: TaskUpdate):
    """Replace the title and completion status of an existing task."""
    updated_task = storage.update_task(task_id, task_update)
    return {"message": "Task updated successfully", "task": updated_task}


@router.delete(
    "/tasks/{task_id}",
    summary="Delete a task",
    response_description="Confirmation that the task was deleted",
    responses=NOT_FOUND,
)
def delete_task(task_id: int):
    """Permanently delete a task by its ID."""
    storage.delete_task(task_id)
    return {"message": "Task deleted successfully"}
