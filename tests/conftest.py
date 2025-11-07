import pytest

from utils.helpers import get_base_url, api_key_header


@pytest.fixture(scope="session")
def base_url():
    """Base URL for API tests."""
    return get_base_url()


@pytest.fixture(scope="session")
def default_headers():
    """Common headers for requests."""
    return api_key_header()

