from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_deve_listar_usuario():
    response = client.get('/usuario')
    assert response.status_code == 200
    assert response.json() == [{"1": "Karol"}, {"2": "Ailton"}]
