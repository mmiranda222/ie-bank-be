from iebank_api import app
import pytest

def test_hello_world():
    """
    GIVEN a Flask application
    WHEN the root endpoint is requested (GET)
    THEN check that the response message is 'Hello, World!' and the status code is 200
    """
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data == b'Hello, World!'

def test_skull():
    """
    GIVEN a Flask application
    WHEN the '/skull' page is requested (GET)
    THEN check that the response message is correct and the status code is 200
    """
    with app.test_client() as client:
        response = client.get('/skull')
        assert response.status_code == 200
        assert b'Hi! This is the BACKEND SKULL!' in response.data

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'country': 'Spain', 'currency': '€'})
    assert response.status_code == 200

def test_get_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is requested with a specific account ID (GET)
    THEN check that the response contains the details of the account
    """
    testing_client.post("/accounts", json={"name": "Test", "country": "Test", "currency": "$"})
    response = testing_client.get('/accounts/1') 
    assert response.status_code == 200
    assert b'Test' in response.data

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN request is made to the '/accounts/<id>' endpoint with a specific account ID and updated data (PUT)
    THEN verify that the account details are successfully updated
    """
    testing_client.post("/accounts", json={"name": "Test", "country": "Test", "currency": "$"})
    data = {'name': 'Updated Name'}
    response = testing_client.put('/accounts/1', json=data)  
    assert response.status_code == 200
    assert b'Updated Name' in response.data

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN request is made to the '/accounts/<id>' (DELETE)
    THEN check that the account corresponding to the provided ID is deleted
    """
    testing_client.post("/accounts", json={"name": "Test", "country": "Testland", "currency": "$"})
    response = testing_client.delete("/accounts/1")
    assert response.status_code == 200



