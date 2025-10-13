import uuid
import os

from dotenv import load_dotenv

def unique_email() -> str:
    """Generate a unique email for test users."""
    return f"test_{uuid.uuid4().hex[:8]}@example.com"


def get_base_url() -> str:
    """Return the API base URL from environment or default."""
    return os.getenv("BASE_URL", "http://localhost:8000")


def api_key_header() -> dict:
    """Optional API key header for endpoints that need it."""
    load_dotenv()
    key = os.getenv("API_KEY")
    return {"X-API-Key": key} if key else {}