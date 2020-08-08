import pytest, requests

# pytest_plugins = ["docker_compose"]

def test_mock_api():
    resp = requests.get('http://localhost:8083/?name=bob')
    resp.raise_for_status()
    assert True
