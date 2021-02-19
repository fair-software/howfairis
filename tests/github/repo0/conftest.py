import pytest
import requests_mock
from requests_mock.mocker import Mocker
from howfairis.code_repository_platforms import Platform
from tests.helpers import get_urls


@pytest.fixture
def mocker() -> Mocker:

    """This mock aims to reflect the state of a fictious repository at
    https://github.com/owner-doesnt-exist/repo-doesnt-exist which does not exist"""

    with requests_mock.Mocker() as m:
        repo, raw, api = get_urls(Platform.GITHUB, owner="owner-doesnt-exist", repo="repo-doesnt-exist")
        m.get(repo, status_code=404)
        m.get(raw + "/master/.howfairis.yml", status_code=404)
        m.get(raw + "/master/.zenodo.json", status_code=404)
        m.get(raw + "/master/codemeta.json", status_code=404)
        m.get(raw + "/master/CITATION.cff", status_code=404)
        m.get(raw + "/master/CITATION", status_code=404)
        m.get(raw + "/master/README.md", status_code=404)
        m.get(raw + "/master/README.rst", status_code=404)
        m.get(api + "/license", status_code=404)
        m.get(api, status_code=404)
        return m
