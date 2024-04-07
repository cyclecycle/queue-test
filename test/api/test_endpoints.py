import httpx

def test_enqueue_endpoint():
    response = httpx.post("http://api:8000/enqueue", json={"queries": ["test query",]})
    print(response.json())
    assert response.status_code == 200

