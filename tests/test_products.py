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