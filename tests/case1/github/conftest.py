import pytest
import requests_mock
from requests_mock.mocker import Mocker
from howfairis.code_repository_platforms import Platform
from tests.helpers import get_urls
from tests.helpers import load_frontend_files_from_local_data


@pytest.fixture
def mocker() -> Mocker:
    """This mock aims to reflect the state of a fictious repository at https://github.com/fair-software/repo1
    without any files in it"""

    frontend_files = load_frontend_files_from_local_data(__file__)
    default_branch_response = {"default_branch": "master"}

    with requests_mock.Mocker() as m:
        repo, raw, api, reuse_url = get_urls(
            Platform.GITHUB, owner="fair-software", repo="repo1"
        )
        m.get(api, status_code=200, json=default_branch_response)
        m.get(api + "/license", status_code=200)
        m.get(raw + "/master/.howfairis.yml", status_code=404)
        m.get(raw + "/master/.zenodo.json", status_code=404)
        m.get(raw + "/master/CITATION.cff", status_code=404)
        m.get(raw + "/master/CITATION", status_code=404)
        m.get(raw + "/master/codemeta.json", status_code=404)
        m.get(raw + "/master/README.rst", status_code=404)
        m.get(raw + "/master/README.md", status_code=404)
        m.get(raw + "/master/this/path/does-not-exist/.howfairis.yml", status_code=404)
        m.get(raw + "/master/this/path/does-not-exist/.zenodo.json", status_code=404)
        m.get(raw + "/master/this/path/does-not-exist/CITATION.cff", status_code=404)
        m.get(raw + "/master/this/path/does-not-exist/CITATION", status_code=404)
        m.get(raw + "/master/this/path/does-not-exist/codemeta.json", status_code=404)
        m.get(raw + "/master/this/path/does-not-exist/README.md", status_code=404)
        m.get(raw + "/master/this/path/does-not-exist/README.rst", status_code=404)
        m.get(repo, status_code=200, text=frontend_files["/index.html"])
        m.get(
            reuse_url,
            status_code=200,
            text=frontend_files["/reuse.json"],
        )

        return m
