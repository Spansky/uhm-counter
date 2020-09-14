from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"counter": 0}

def test_post_increment_once():
    response = client.post("/increment")
    assert response.status_code == 200
    assert response.json() == {"counter": 1}

def test_get_after_increment():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"counter": 1}

def test_post_increment_10_times():
    for i in range(1,11):
        response = client.post("/increment")
        assert response.json() == {"counter": i+1}
    response = client.get("/")
    assert response.json() == {"counter": 11}

def test_post_reset():
    response = client.post("/reset")
    assert response.status_code == 200
    assert response.json() == {"counter": 0}

