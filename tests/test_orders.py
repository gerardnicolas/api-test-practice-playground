import requests

from utils.helpers import unique_email


def test_create_order_for_user(base_url, default_headers):
    # Create user (creating user to generate user_id)
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

    # Create order for user
    params = {"user_id": user_id}
    payload = [
        {
            "product_id": 2,
            "quantity": 5
        }
    ]

    res = requests.post(f"{base_url}/v1/users/{user_id}/orders", headers=default_headers, params=params, json=payload)
    assert res.status_code == 201, f"Expected 201, instead got {res.status_code}"
    data = res.json()
    assert isinstance(data, dict)

    # Assert keys are present in response
    assert "order_id" in data
    assert "total" in data
    assert data["status"] == "pending", f"Expected status is 'pending', got {data["status"]} instead" # Initial status upon order creation is 'pending'