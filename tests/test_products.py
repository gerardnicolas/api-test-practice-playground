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