import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_create_task_success():
    payload = {
        "title": "Тестова таска",
        "description": "Це перевірка нашого API",
        "state": "pending"
    }

    response = client.post("/create_task", json=payload)

    assert response.status_code == 200 or response.status_code == 201

    data = response.json()
    assert data["title"] == "Тестова таска"
    assert data["state"] == "pending"

def test_create_task_missing_title():
    payload = {
        "description": "Забули назву",
        "state": "pending"
    }

    response = client.post("/create_task", json=payload)

    assert response.status_code == 422

def test_create_task_invalid_state():
    payload = {
        "title": "Таска з неправильним статусом",
        "description": "Статус не відповідає допустимим значенням",
        "state": "invalid_state"
    }

    response = client.post("/create_task", json=payload)

    assert response.status_code == 422

def test_update_task_success():
    create_payload = {
        "title": "Таска для оновлення",
        "description": "Це тестова таска для оновлення",
        "state": "pending"
    }
    create_response = client.post("/create_task", json=create_payload)
    assert create_response.status_code == 200 or create_response.status_code == 201

    update_payload = {
        "title": "Оновлена таска",
        "description": "Опис оновлений",
        "state": "in_progress"
    }
    update_response = client.put(f"/update_task/1", json=update_payload)
    assert update_response.status_code == 200

    updated_data = update_response.json()
    assert updated_data["title"] == "Оновлена таска"
    assert updated_data["state"] == "in_progress"

def test_update_task_not_found():
    update_payload = {
        "title": "Таска, яка не існує",
        "description": "Спроба оновити неіснуючу таску",
        "state": "pending"
    }
    response = client.put("/update_task/9999", json=update_payload)
    assert response.status_code == 404

def test_delete_task_success():
    create_payload = {
        "title": "Таска для видалення",
        "description": "Це тестова таска для видалення",
        "state": "pending"
    }
    create_response = client.post("/create_task", json=create_payload)
    assert create_response.status_code == 200 or create_response.status_code == 201

    delete_response = client.delete(f"/delete_task/1")
    assert delete_response.status_code == 204

def test_delete_task_not_found():
    response = client.delete("/delete_task/9999")
    assert response.status_code == 404
