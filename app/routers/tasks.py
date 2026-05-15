from fastapi import APIRouter
from app.models import TaskCreate, TaskUpdate
import app.storage as storage

router = APIRouter()


@router.get("/tasks")
def get_tasks():
    return {"tasks": storage.list_tasks()}


@router.post("/tasks")
def create_task(task: TaskCreate):
    new_task = storage.create_task(task)
    return {"message": "Task created successfully", "task": new_task}


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    updated_task = storage.update_task(task_id, task_update)
    return {"message": "Task updated successfully", "task": updated_task}


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    storage.delete_task(task_id)
    return {"message": "Task deleted successfully"}
