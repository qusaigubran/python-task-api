<div align="center">

# 🐍 Python Task API

**A clean, tested REST API for managing tasks — built with FastAPI and SQLite.**

[![CI](https://github.com/qusaigubran/python-task-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/qusaigubran/python-task-api/actions/workflows/python-app.yml)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Pytest](https://img.shields.io/badge/Tests-28_passing-0EA5E9?style=flat-square&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square&logo=docker&logoColor=white)

[Quick start](#-quick-start) · [API reference](#-api-reference) · [Interactive docs](#-interactive-docs) · [Testing](#-testing) · [Project structure](#-project-structure)

</div>

---

## ✨ Overview

Python Task API is a backend project focused on the fundamentals of building a real API:

- **Routing** with FastAPI and a dedicated tasks router
- **Validation** of request bodies with Pydantic models
- **Persistence** in a local SQLite database
- **Full CRUD** — create, list, update, and delete tasks
- **Automated tests** with pytest (28 tests across all endpoints)
- **CI** with GitHub Actions on every push and pull request
- **Docker** support for a one-command local setup

---

## 🚀 Quick start

### Option 1 — Run locally

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # macOS / Linux
.venv\Scripts\Activate.ps1         # Windows PowerShell

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
uvicorn app.main:app --reload
```

### Option 2 — Run with Docker

```bash
docker compose up --build
```

The API is now available at **http://127.0.0.1:8000**.

---

## 📖 Interactive docs

FastAPI generates live documentation from the code. Once the server is running, open:

| Docs | URL | Best for |
| :--- | :--- | :--- |
| **Swagger UI** | http://127.0.0.1:8000/docs | Trying endpoints directly in the browser |
| **ReDoc** | http://127.0.0.1:8000/redoc | Reading the full API reference |
| **OpenAPI schema** | http://127.0.0.1:8000/openapi.json | Importing into Postman or other tools |

Endpoints are grouped into **Health** and **Tasks**, each with a summary, description, request examples, and documented error responses.

---

## 🔌 API reference

| Method | Endpoint | Description | Success | Errors |
| :---: | :--- | :--- | :---: | :---: |
| `GET` | `/` | Health check — confirms the API is running | `200` | — |
| `GET` | `/tasks` | List all tasks, ordered by ID | `200` | — |
| `POST` | `/tasks` | Create a new task | `200` | `422` |
| `PUT` | `/tasks/{task_id}` | Update a task's title and status | `200` | `404` · `422` |
| `DELETE` | `/tasks/{task_id}` | Delete a task | `200` | `404` |

### Task object

| Field | Type | Required | Notes |
| :--- | :--- | :---: | :--- |
| `id` | integer | — | Assigned automatically |
| `title` | string | ✅ | Short description of the task |
| `completed` | boolean | ❌ | Defaults to `false` on create |

<details>
<summary><b>Examples</b></summary>

**Create a task**

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Study FastAPI"}'
```

```json
{
  "message": "Task created successfully",
  "task": { "id": 1, "title": "Study FastAPI", "completed": false }
}
```

**List tasks**

```bash
curl http://127.0.0.1:8000/tasks
```

```json
{
  "tasks": [
    { "id": 1, "title": "Study FastAPI", "completed": false }
  ]
}
```

**Update a task**

```bash
curl -X PUT http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Study FastAPI routing", "completed": true}'
```

```json
{
  "message": "Task updated successfully",
  "task": { "id": 1, "title": "Study FastAPI routing", "completed": true }
}
```

**Delete a task**

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

```json
{ "message": "Task deleted successfully" }
```

**Task not found**

```json
{ "detail": "Task not found" }
```

</details>

---

## 🧪 Testing

```bash
pytest -q
```

The test suite covers the health endpoint, listing, creating, updating, and deleting tasks, including `404` cases for missing tasks.

> **Note:** tests run against the same local database file (`data/tasks.db`) and reset it before each test, so any tasks you created locally will be cleared.

### Continuous integration

Every push and pull request to `main` runs the **Python Task API CI** workflow, which:

1. Installs dependencies on Python 3.12
2. Checks syntax and verifies the app imports
3. Starts the server and runs the full pytest suite
4. Smoke-tests the live health endpoint

---

## 🗂️ Project structure

```text
python-task-api/
├── app/
│   ├── main.py              # FastAPI app, docs metadata, health endpoint
│   ├── models.py            # Pydantic request models
│   ├── storage.py           # SQLite access layer
│   └── routers/
│       └── tasks.py         # /tasks endpoints
├── tests/
│   └── test_main.py         # pytest suite
├── .github/workflows/
│   └── python-app.yml       # CI pipeline
├── .devcontainer/           # Dev container configuration
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
└── requirements.txt
```

---

## 🛣️ Roadmap

- [ ] `GET /tasks/{task_id}` to fetch a single task
- [ ] `PATCH /tasks/{task_id}` for partial updates
- [ ] Stricter validation (e.g. non-empty titles)
- [ ] `201 Created` status for new tasks
- [ ] Separate database for tests
- [ ] API versioning and authentication

---

<div align="center">

Built by **[Qusai Gubran](https://github.com/qusaigubran)** · [qusai.m.gubran@gmail.com](mailto:qusai.m.gubran@gmail.com)

</div>
