
import pytest
from CommonFunctions.auth_helper import get_jwt_token, get_oauth_token
from CommonFunctions.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def access_token():
    logger.info("Generating access token from conftest fixture...")
    username = get_jwt_token()
    token = get_oauth_token(username)
    logger.info("Access token acquired successfully.")
    return token
