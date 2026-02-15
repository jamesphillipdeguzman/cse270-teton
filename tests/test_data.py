# test_data.py
import pytest
import requests

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

@pytest.fixture
def mock_requests_get(monkeypatch):
    # The fake response we want requests.get to return
    response_json = {"businesses":[{"name":"Teton Elementary"}]}
    mock_response = MockResponse(response_json)

    # Patch requests.get to always return our mock_response
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: mock_response)

    # Optionally return the mock response to the test
    return mock_response

def test_data_endpoint(mock_requests_get):
    # Make the HTTP GET request
    response = requests.get('http://127.0.0.1:8000/data/all')

    # Verify the response status code
    assert response.status_code == 200

    # Verify the response content
    data = response.json()
    assert isinstance(data, dict)
    assert 'businesses' in data
    businesses = data['businesses']
    assert isinstance(businesses, list)
    assert len(businesses) > 0
    first_business = businesses[0]
    assert isinstance(first_business, dict)
    assert 'name' in first_business
    assert first_business['name'] == 'Teton Elementary'
