from fastapi import FastAPI
from app.routers import tasks

DESCRIPTION = """
A small REST API for managing tasks, built with **FastAPI** and **SQLite**.

### What you can do
- **List** all tasks
- **Create** a task with a title and completion status
- **Update** a task by its ID
- **Delete** a task by its ID

Tasks are stored in a local SQLite database (`data/tasks.db`), so they persist between restarts.

Use **Try it out** on any endpoint below to send a real request.
"""

TAGS_METADATA = [
    {"name": "Health", "description": "Check that the API is up and running."},
    {"name": "Tasks", "description": "Create, read, update, and delete tasks."},
]

app = FastAPI(
    title="Python Task API",
    description=DESCRIPTION,
    version="1.0.0",
    openapi_tags=TAGS_METADATA,
    contact={
        "name": "Qusai Gubran",
        "url": "https://github.com/qusaigubran",
        "email": "qusai.m.gubran@gmail.com",
    },
    swagger_ui_parameters={
        "docExpansion": "list",
        "defaultModelsExpandDepth": 0,
        "displayRequestDuration": True,
        "tryItOutEnabled": True,
        "syntaxHighlight.theme": "monokai",
    },
)


@app.get(
    "/",
    tags=["Health"],
    summary="Health check",
    response_description="A message confirming the API is running",
)
def home():
    """Return a simple message to confirm the API is running."""
    return {"message": "Python Task API is running"}


app.include_router(tasks.router)
