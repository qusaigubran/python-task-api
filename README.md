# Python Task API

A simple learning project for building a task management API with **Python** and **FastAPI**.

This project focuses on backend fundamentals: routing, validation, API design, in-memory data handling, and clear documentation.

---

## Purpose

The goal of this project is not to build a production system yet. The goal is to practice how backend APIs are structured step by step.

Core learning areas:

- Python backend development
- FastAPI basics
- REST API design
- Request and response validation
- CRUD operations
- Simple testing with pytest
- Clean project documentation

---

## Features

- Create a task
- List all tasks
- Get a task by ID
- Update a task
- Delete a task
- Health check endpoint

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest

---

## Project Structure

```text
python-task-api/
├── app/
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Run Locally

### 1. Create a virtual environment

```bash
python -m venv .venv
```

This creates an isolated Python environment for the project.

### 2. Activate the virtual environment

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

This activates the local environment so packages install inside the project.

macOS / Linux:

```bash
source .venv/bin/activate
```

This activates the local environment on Unix-based systems.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This installs FastAPI, Uvicorn, and testing dependencies.

### 4. Start the API server

```bash
uvicorn app.main:app --reload
```

This runs the development server with automatic reload.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API status |
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{task_id}` | Get one task |
| PUT | `/tasks/{task_id}` | Update one task |
| DELETE | `/tasks/{task_id}` | Delete one task |

---

## Example Task JSON

```json
{
  "title": "Study FastAPI",
  "description": "Practice building a simple API",
  "completed": false
}
```

---

## Run Tests

```bash
pytest
```

This runs the project test suite.

---

## Current Status

Learning project — basic API structure completed. Future improvements may include database storage, authentication, Docker support, and CI checks.
