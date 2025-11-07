import pytest
import requests
from utils.helpers import unique_sku


@pytest.mark.products
@pytest.mark.smoke
def test_product_flow(base_url, default_headers):
    """End-to-end test for product creation."""
    # Create user
    prod_id = unique_sku()
    payload = {
        "sku": prod_id,
        "name": "Test Prod",
        "description": "Product Desc",
        "price": 9,
        "category": "General",
        "stock": 99
    }
    r = requests.post(f"{base_url}/v1/products", json=payload, headers=default_headers)
    assert r.status_code == 201
