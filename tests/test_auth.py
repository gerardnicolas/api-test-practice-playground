import pytest
import requests
from utils.helpers import unique_email


@pytest.mark.auth
def test_user_flow(base_url, default_headers):
    """End-to-end test for user creation and token login."""
    # Create user
    email = unique_email()
    pw = "pw123"
    payload = {"email": email, "full_name": "Test User", "password": pw}
    r = requests.post(f"{base_url}/v1/users", json=payload, headers=default_headers)
    assert r.status_code == 201
    assert "id" in r.json()
    assert "email" in r.json()

    # Login to get bearer token
    r = requests.post(f"{base_url}/token", data={"username": email, "password": pw})
    assert r.status_code == 200
    token = r.json()["access_token"]

    # Validate user using bearer token
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"{base_url}/v1/me", headers=headers)
    assert r.status_code == 200
    assert r.json()["email"] == email
