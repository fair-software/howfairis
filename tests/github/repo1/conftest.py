import pytest
from tests.helpers import load_files_from_local_data
from tests.helpers import get_urls
from howfairis.code_repository_platforms import Platform
import requests_mock
from requests_mock.mocker import Mocker


@pytest.fixture
def mocker() -> Mocker:

    """This mock aims to reflect the state of the repository at
    https://github.com/fair-software/badge/tree/b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a"""

    repo_files = load_files_from_local_data(__file__, dir_type="repo")
    default_branch_response = {"default_branch": "master"}

    with requests_mock.Mocker() as m:
        repo, raw, api = get_urls(Platform.GITHUB, owner="fair-software", repo="badge")
        m.get(repo, status_code=200, text=repo_files["/index.html"])
        m.get(raw + "/master/.howfairis.yml", status_code=404)
        m.get(raw + "/master/.zenodo.json", status_code=404)
        m.get(raw + "/master/codemeta.json", status_code=404)
        m.get(raw + "/master/CITATION.cff", status_code=200, text=repo_files["/CITATION.cff"])
        m.get(raw + "/master/CITATION", status_code=404)
        m.get(raw + "/master/README.md", status_code=200, text=repo_files["/README.md"])
        m.get(raw + "/master/README.rst", status_code=404)
        m.get(api + "/license", status_code=200)
        m.get(api, status_code=200, json=default_branch_response)
        return m
