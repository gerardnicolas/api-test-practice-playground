import uuid
import os


def unique_email() -> str:
    """Generate a unique email for test users."""
    return f"test_{uuid.uuid4().hex[:8]}@example.com"


def unique_sku() -> str:
    """Generate a unique product ID of test products."""
    return f"sku-{uuid.uuid4().hex[:3]}"


def get_base_url() -> str:
    """Return the API base URL from environment or default."""
    return os.getenv("BASE_URL")


def api_key_header() -> dict:
    """Optional API key header for endpoints that need it."""
    key = os.getenv("API_KEY")
    return {"X-API-Key": key} if key else {}
