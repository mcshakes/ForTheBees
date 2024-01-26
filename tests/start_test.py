import pytest
from app import app

def test_get_version():
    response = app.test_client().get('/version')
    assert response.status_code == 200