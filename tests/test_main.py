from app import app

def test_homepage_loads():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"<form" in response.data  # checks that your form is present

