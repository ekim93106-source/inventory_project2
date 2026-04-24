from app import app

def test_get_inventory():
    client = app.test_client()
    response = client.get('/inventory')
    assert response.status_code == 200

def test_add_item():
    client = app.test_client()
    response = client.post('/inventory', json={
        "id": 3,
        "name": "Sugar",
        "price": 150,
        "stock": 5
    })
    assert response.status_code == 201