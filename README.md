# Python Task API

A simple learning project for building a task management API with **Python**, **FastAPI**, and **SQLite**.

This project focuses on backend fundamentals: routing, validation, API design, persistent local storage, CRUD operations, and automated testing.

---

## Purpose

The goal of this project is to practice how backend APIs are structured step by step.

Core learning areas:

- Python backend development
- FastAPI routing
- REST API design
- Request and response validation with Pydantic
- SQLite database storage
- CRUD operations
- Automated testing with pytest
- Clean project documentation

---

## Features

- Home endpoint to confirm the API is running
- Create a task
- List all tasks
- Update a task
- Delete a task
- SQLite-based task storage
- Test coverage for main task flows

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn
- Pytest
- HTTPX

---

## Project Structure

```text
python-task-api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   └── routers/
│       └── tasks.py
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

This installs the API and testing dependencies.

### 4. Start the API server

```bash
uvicorn app.main:app --reload
```

This runs the development server with automatic reload.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Confirm the API is running |
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update one task |
| DELETE | `/tasks/{task_id}` | Delete one task |

---

## Example Task JSON

```json
{
  "title": "Study FastAPI",
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

Learning project — basic FastAPI structure, SQLite storage, and task-flow tests are included.

Future improvements may include:

- `GET /tasks/{task_id}` endpoint
- Partial updates with `PATCH`
- Better validation rules
- Docker support
- GitHub Actions CI
- API versioning
- Authentication
