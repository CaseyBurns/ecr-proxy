import pytest, requests

def test_health():
    resp = requests.get('http://localhost:443/health')
    assert resp.status_code == 200

def test_version_check():
    resp = requests.get('http://localhost:443/v2/')
    assert resp.status_code == 200


def test_list_catalog():
    resp = requests.get('http://localhost:443/v2/_catalog')
    assert resp.status_code == 200

def test_denied():
    resp = requests.get('http://localhost:443/v2/token-expired/tags/list')
    assert resp.status_code == 403
