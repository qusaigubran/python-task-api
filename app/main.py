from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="python Task API")

tasks = []
next_id = 1

class TaskCreate(BaseModel):
    title : str
    completed: bool = False

@app.get("/")
def home ():
    return {"message": "Python Task API is  running"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "completed": task.completed
    }
    tasks.append(new_task)
    next_id += 1
    return {"message": "Task created successfully", "task": new_task}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
