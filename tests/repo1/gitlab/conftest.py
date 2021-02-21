import pytest
from tests.helpers import load_repo_files_from_local_data
from tests.helpers import get_urls
from howfairis.code_repository_platforms import Platform
import requests_mock
from requests_mock.mocker import Mocker


@pytest.fixture
def mocker() -> Mocker:

    """This mock aims to reflect the state of a fictious repository at https://gitlab.com/owner1/repo1 with
    contents to maximize the number of tests that will be True"""

    repo_files = load_repo_files_from_local_data(__file__)
    default_branch_response = {"default_branch": "master"}

    with requests_mock.Mocker() as m:
        repo, raw, api = get_urls(Platform.GITLAB, owner="owner1", repo="repo1")
        m.get(api, status_code=200, json=default_branch_response)
        m.get(api + "/repository/tree", status_code=200)
        m.get(raw + "/master/.howfairis.yml", status_code=200, text=repo_files["/.howfairis.yml"])
        m.get(raw + "/master/.zenodo.json", status_code=200, text=repo_files["/.zenodo.json"])
        m.get(raw + "/master/CITATION", status_code=200, text=repo_files["/CITATION"])
        m.get(raw + "/master/CITATION.cff", status_code=200, text=repo_files["/CITATION.cff"])
        m.get(raw + "/master/codemeta.json", status_code=200, text=repo_files["/codemeta.json"])
        m.get(raw + "/master/README.rst", status_code=200, text=repo_files["/README.rst"])
        m.get(repo, status_code=200, text=repo_files["/index.html"])

        return m
