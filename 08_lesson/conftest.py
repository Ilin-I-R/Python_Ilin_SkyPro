import pytest
import requests
from config import BASE_URL, API_KEY
from project_api import ProjectAPI


@pytest.fixture
def headers():
    return {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def project_api(base_url, headers):
    return ProjectAPI(base_url, headers)


@pytest.fixture
def test_project(project_api):
    response = project_api.create_project("Test Project")
    project_data = response.json()
    yield project_data
    try:
        requests.delete(
            project_api.base_url + "/projects/" + project_data["id"],
            headers=project_api.headers
        )
    except Exception:
        pass
