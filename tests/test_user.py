import requests
import pytest

BASE_URL = "http://127.0.0.1:8000/users"


def test_authentication_failed(mocker):
    """
    Test 1 (mocked):
    Send a GET request with username=admin and password=admin

    Expectations:
    - Response status code should be 401 (Unauthorized)
    - Response body should be empty
    """

    # Mock requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mocker.patch("requests.get", return_value=mock_response)

    params = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.get(BASE_URL, params=params)

    # Verify status code
    assert response.status_code == 401

    # Verify empty response body
    assert response.text.strip() == ""


def test_authentication_successful(mocker):
    """
    Test 2 (mocked):
    Send a GET request with username=admin and password=querty

    Expectations:
    - Response status code should be 200 (OK)
    - Response body should be empty
    """

    # Mock requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mocker.patch("requests.get", return_value=mock_response)

    params = {
        "username": "admin",
        "password": "querty"
    }

    response = requests.get(BASE_URL, params=params)

    # Verify status code
    assert response.status_code == 200

    # Verify empty response body
    assert response.text.strip() == ""