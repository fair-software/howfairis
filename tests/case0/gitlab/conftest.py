import pytest
from tests.helpers import get_urls
from howfairis.code_repository_platforms import Platform
import requests_mock
from requests_mock.mocker import Mocker


@pytest.fixture
def mocker() -> Mocker:

    """This mock aims to reflect the state of a fictious repository at
    https://gitlab.com/owner-doesnt-exist/repo-doesnt-exist"""

    with requests_mock.Mocker() as m:
        _, _, api = get_urls(Platform.GITLAB, owner="owner-doesnt-exist", repo="repo-doesnt-exist")
        m.get(api, status_code=404)
        return m
