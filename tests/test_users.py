import requests

from utils.helpers import unique_email


def test_user_lifecycle_end_to_end(base_url,default_headers):
    """End-to-end test for creating, getting/reading, updating, and deleting users."""

    # List users
    params = {"skip": 0, "limit": 50}
    res = requests.get(f"{base_url}/v1/users", headers=default_headers, params=params)
    assert res.status_code == 200, f"Expected 200, got {res.status_code} instead"
    data = res.json()
    assert isinstance(data, list)
    assert len(data) > 0

    # Assert that each item has expected keys
    for item in data:
        assert "id" in item, "Missing 'id' in response"
        assert "email" in item, "Missing 'email' in response"
        assert "full_name" in item, "Missing 'full_name' in response"

    # Create user
    create_params = {"accept-version": "v1"}
    email = unique_email()
    payload = {
        "email": email,
        "full_name": "John Doe",
        "role": "customer",
        "password": "randomPassword"
    }

    res = requests.post(f"{base_url}/v1/users", headers=default_headers, params=create_params, json=payload)
    assert res.status_code == 201, f"Expected 201, got {res.status_code} instead"
    data = res.json()
    assert isinstance(data, dict)

    # Assert that key is present in response
    assert "id" in data
    assert "email" in data

    # Store created user id and email
    user_id = data["id"]
    user_email = data["email"]

    # Get user by id
    getuser_params = {"user_id": user_id}
    res = requests.get(f"{base_url}/v1/users/{user_id}", headers=default_headers, params=getuser_params)
    assert res.status_code == 200, f"Expected 200, got {res.status_code} instead"
    data = res.json()
    assert isinstance(data, dict)

    # Assert that key is present in response
    assert "id" in data
    assert "email" in data
    assert "full_name" in data

    # Store response user id and email
    response_user_id = data["id"]
    response_email = data["email"]

    # Assert that response user id and email is equivalent to created user id and email
    assert response_user_id == user_id, f"Expected {user_id}, got {response_user_id} instead"
    assert response_email == user_email, f"Expected {user_email}, got {response_email} instead"

    # Update user
    update_params = {"user_id": user_id}
    payload = {
        "full_name": "Jane Doe",
        "password": "122333",
        "role": "vip_customer"
    }

    res = requests.put(f"{base_url}/v1/users/{user_id}", headers=default_headers, params=update_params, json=payload)
    data = res.json()

    assert res.status_code == 200, f"Expected 200, got {res.status_code} instead"
    assert isinstance(data, dict)

    # Assert that key is present in response
    assert "id" in data
    assert "email" in data
    assert "full_name" in data
    assert "role" in data

    # Assert that response full name and role is equivalent to payload full name and role
    assert data["full_name"] == payload["full_name"]
    assert data["role"] == payload["role"]

    # Soft delete user
    delete_params = {"user_id": user_id}

    res = requests.delete(f"{base_url}/v1/users/{user_id}", headers=default_headers, params=delete_params)

    assert res.status_code == 204, f"Expected 204, got {res.status_code} instead"
    # assert data["deleted"] == True