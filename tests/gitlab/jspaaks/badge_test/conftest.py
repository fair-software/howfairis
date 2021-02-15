import pytest
from tests.helpers import load_files_from_local_data
from tests.helpers import get_urls
from howfairis.code_repository_platforms import Platform
import requests_mock
from requests_mock.mocker import Mocker


@pytest.fixture
def mocker() -> Mocker:

    """This mock aims to reflect the state of the repository at
    https://gitlab.com/jspaaks/badge-test/-/tree/472713282fde87fa4c8e5116e46229c094c3c4ec"""

    default_branch_response = {"default_branch": "master"}
    data = load_files_from_local_data(__file__)

    with requests_mock.Mocker() as m:
        repo, raw, api = get_urls(Platform.GITLAB, owner="jspaaks", repo="badge-test")

        m.get(repo, status_code=200, text=data["/index.html"])
        m.get(raw + "/master/.howfairis.yml", status_code=404)
        m.get(raw + "/master/.zenodo.json", status_code=404)
        m.get(raw + "/master/codemeta.json", status_code=404)
        m.get(raw + "/master/CITATION.cff", status_code=404)
        m.get(raw + "/master/CITATION", status_code=404)
        m.get(raw + "/master/README.md", status_code=200, text=data["/README.md"])
        m.get(raw + "/master/README.rst", status_code=404)
        m.get(api + "/repository/tree", status_code=200)
        m.get(api, status_code=200, json=default_branch_response)
        return m
