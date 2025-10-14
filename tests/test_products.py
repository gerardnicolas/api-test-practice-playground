import requests

def test_list_products(base_url, default_headers):
    # Add params for page and per_page
    params = {"page": 1, "per_page": 20}

    # GET Request
    res = requests.get(f"{base_url}/v1/products", headers=default_headers, params=params)

    assert res.status_code == 200
    data = res.json()

    # Assert that 3 items are returned (as expected)
    items = data["items"]
    assert len(items) == 3

def test_create_product(base_url, default_headers):
    params = {"accept-version": "v1"}
    payload = {
        "sku": "SKU-004",
        "name": "Tasty Bites Dog Treats",
        "description": "Delicious",
        "price": 25,
        "category": "food",
        "stock": 54
    }

    res = requests.post(f"{base_url}/v1/products", headers=default_headers, params=params, json=payload)

    assert res.status_code == 201, f"Expected 201, got {res.status_code}"
    data = res.json()

    # Assert that response matches payload
    assert data["sku"] == payload["sku"]

def test_delete_product(base_url, default_headers):
    product_id = 4

    res = requests.delete(f"{base_url}/v1/products/{product_id}", headers=default_headers)

    assert res.status_code == 204, f"Expected 204, got {res.status_code}"

def test_get_product(base_url, default_headers):
    product_id = 3

    res = requests.get(f"{base_url}/v1/products/{product_id}", headers=default_headers)

    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    data = res.json()

    assert data["id"] == product_id

def test_update_product(base_url, default_headers):
    product_id = 3
    payload = {
        "name": "Gold Nylon Leash",
        "description": "Strong, 3.5m",
        "price": 100,
        "category": "pet",
        "stock": 10
    }

    res = requests.put(f"{base_url}/v1/products/{product_id}", headers=default_headers, json=payload)

    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    data = res.json()

    assert data["name"] == "Gold Nylon Leash"
    assert data["price"] == 100
    assert data["stock"] == 10

def test_product_flow(base_url, default_headers):
    """End-to-end test for creating, getting/reading, updating, and deleting product."""
    # Create a product
    params = {"accept-version": "v1"}
    payload = {
        "sku": "SKU-005",
        "name": "Canned Wet Food",
        "description": "Yummy",
        "price": 34,
        "category": "food",
        "stock": 18
    }

    res = requests.post(f"{base_url}/v1/products", headers=default_headers, params=params, json=payload)

    assert res.status_code == 201, f"Expected 201, got {res.status_code}"
    data = res.json()
    product_id = data.get("id")
    assert product_id, f"Product ID missing in response"

    # Get product
    res = requests.get(f"{base_url}/v1/products/{product_id}", headers=default_headers)

    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    data = res.json()

    assert data["id"] == product_id

    # Update product
    payload = {
        "name": "Special Canned Wet Food",
        "description": "Extra Yummy",
        "price": 50,
        "category": "food",
        "stock": 31
    }

    res = requests.put(f"{base_url}/v1/products/{product_id}", headers=default_headers, json=payload)

    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    data = res.json()

    assert data["name"] == "Special Canned Wet Food"
    assert data["price"] == 50
    assert data["stock"] == 31

    # Delete product
    res = requests.delete(f"{base_url}/v1/products/{product_id}", headers=default_headers)

    assert res.status_code == 204, f"Expected 204, got {res.status_code}"