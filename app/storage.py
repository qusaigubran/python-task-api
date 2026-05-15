from fastapi import HTTPException
from app.models import TaskCreate, TaskUpdate

tasks = []
next_id = 1


def reset_state():
    global next_id
    tasks.clear()
    next_id = 1


def list_tasks():
    return tasks


def create_task(task_create: TaskCreate):
    global next_id
    new_task = {
        "id": next_id,
        "title": task_create.title,
        "completed": task_create.completed,
    }
    tasks.append(new_task)
    next_id += 1
    return new_task


def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            task["completed"] = task_update.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")


def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return
    raise HTTPException(status_code=404, detail="Task not found")
