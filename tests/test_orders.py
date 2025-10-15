import requests

from utils.helpers import unique_email


def test_order_flow(base_url, default_headers):
    """End-to-end test for order creation, order status update, and order deletion."""
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

    order_id = data["order_id"]

    # Update order status
    params = {"order_id": order_id}
    payload = {
        "status": "confirmed"
    }

    res = requests.put(f"{base_url}/v1/orders/{order_id}/status", headers=default_headers, params=params, json=payload)
    assert res.status_code == 200, f"Expected 200, instead got {res.status_code}"
    data = res.json()
    assert isinstance(data, dict)

    # Assert keys are present in response
    assert data["status"] == payload["status"], f"{payload["status"]} did not match response: {data["status"]}"
    assert "order_id" in data
    assert "total" in data

    # Delete order
    params = {"order_id": order_id}
    res = requests.delete(f"{base_url}/v1/orders/{order_id}", headers=default_headers, params=params)
    assert res.status_code == 204, f"Expected 204, instead got {res.status_code}"