import pytest
import app.main as main_module
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_state():
    main_module.tasks.clear()
    main_module.next_id = 1


# A. GET /
def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_message_key():
    response = client.get("/")
    assert "message" in response.json()


def test_home_message_indicates_running():
    response = client.get("/")
    assert "running" in response.json()["message"].lower()


# B. GET /tasks initial state
def test_get_tasks_status_code():
    response = client.get("/tasks")
    assert response.status_code == 200


def test_get_tasks_contains_tasks_key():
    response = client.get("/tasks")
    assert "tasks" in response.json()


def test_get_tasks_is_list():
    response = client.get("/tasks")
    assert isinstance(response.json()["tasks"], list)


# C. POST /tasks
def test_create_task_status_code():
    response = client.post("/tasks", json={"title": "Test task", "completed": False})
    assert response.status_code == 200


def test_create_task_contains_message():
    response = client.post("/tasks", json={"title": "Test task", "completed": False})
    assert "message" in response.json()


def test_create_task_response_has_id():
    response = client.post("/tasks", json={"title": "Test task", "completed": False})
    assert "id" in response.json()["task"]


def test_create_task_response_has_title():
    response = client.post("/tasks", json={"title": "Test task", "completed": False})
    assert "title" in response.json()["task"]


def test_create_task_response_has_completed():
    response = client.post("/tasks", json={"title": "Test task", "completed": False})
    assert "completed" in response.json()["task"]


def test_create_task_title_matches():
    response = client.post("/tasks", json={"title": "Buy milk", "completed": False})
    assert response.json()["task"]["title"] == "Buy milk"


def test_create_task_completed_defaults_false():
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.json()["task"]["completed"] is False


# D. GET /tasks after POST
def test_created_task_appears_in_list():
    client.post("/tasks", json={"title": "Visible task", "completed": False})
    response = client.get("/tasks")
    tasks = response.json()["tasks"]
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Visible task"


def test_multiple_tasks_appear_in_list():
    client.post("/tasks", json={"title": "Task one", "completed": False})
    client.post("/tasks", json={"title": "Task two", "completed": True})
    response = client.get("/tasks")
    assert len(response.json()["tasks"]) == 2


# E. DELETE /tasks/{task_id} — existing task
def test_delete_existing_task_status_code():
    post_response = client.post("/tasks", json={"title": "To delete", "completed": False})
    task_id = post_response.json()["task"]["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200


def test_delete_existing_task_confirms_deletion():
    post_response = client.post("/tasks", json={"title": "To delete", "completed": False})
    task_id = post_response.json()["task"]["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert "message" in response.json()


def test_deleted_task_no_longer_in_list():
    post_response = client.post("/tasks", json={"title": "To delete", "completed": False})
    task_id = post_response.json()["task"]["id"]
    client.delete(f"/tasks/{task_id}")
    tasks = client.get("/tasks").json()["tasks"]
    assert all(t["id"] != task_id for t in tasks)


# F. DELETE /tasks/{task_id} — not found
def test_delete_nonexistent_task_status_code():
    response = client.delete("/tasks/999999")
    assert response.status_code == 404


def test_delete_nonexistent_task_detail():
    response = client.delete("/tasks/999999")
    assert response.json()["detail"] == "Task not found"


# G. PUT /tasks/{task_id} — existing task
def test_update_existing_task_status_code():
    post_response = client.post("/tasks", json={"title": "Old title", "completed": False})
    task_id = post_response.json()["task"]["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "New title", "completed": True})
    assert response.status_code == 200


def test_update_existing_task_message():
    post_response = client.post("/tasks", json={"title": "Old title", "completed": False})
    task_id = post_response.json()["task"]["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "New title", "completed": True})
    assert response.json()["message"] == "Task updated successfully"


def test_update_existing_task_id_unchanged():
    post_response = client.post("/tasks", json={"title": "Old title", "completed": False})
    task_id = post_response.json()["task"]["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "New title", "completed": True})
    assert response.json()["task"]["id"] == task_id


def test_update_existing_task_title_changed():
    post_response = client.post("/tasks", json={"title": "Old title", "completed": False})
    task_id = post_response.json()["task"]["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "New title", "completed": True})
    assert response.json()["task"]["title"] == "New title"


def test_update_existing_task_completed_changed():
    post_response = client.post("/tasks", json={"title": "Old title", "completed": False})
    task_id = post_response.json()["task"]["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "New title", "completed": True})
    assert response.json()["task"]["completed"] is True


# H. GET /tasks after PUT
def test_updated_task_appears_in_list():
    post_response = client.post("/tasks", json={"title": "Old title", "completed": False})
    task_id = post_response.json()["task"]["id"]
    client.put(f"/tasks/{task_id}", json={"title": "New title", "completed": True})
    tasks = client.get("/tasks").json()["tasks"]
    updated = next(t for t in tasks if t["id"] == task_id)
    assert updated["title"] == "New title"
    assert updated["completed"] is True


# I. PUT /tasks/{task_id} — not found
def test_update_nonexistent_task_status_code():
    response = client.put("/tasks/999999", json={"title": "Anything", "completed": False})
    assert response.status_code == 404


def test_update_nonexistent_task_detail():
    response = client.put("/tasks/999999", json={"title": "Anything", "completed": False})
    assert response.json()["detail"] == "Task not found"
