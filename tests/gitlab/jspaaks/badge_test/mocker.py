import requests_mock
import pytest


@pytest.fixture
def mocker():
    """This mock aims to reflect the state of the repository at
    https://gitlab.com/jspaaks/badge-test/-/tree/472713282fde87fa4c8e5116e46229c094c3c4ec"""
    with requests_mock.Mocker() as mocker:
        mocker.get("https://gitlab.com/jspaaks/badge-test")
        mocker.get("https://gitlab.com/api/v4/projects/jspaaks%2Fbadge-test", json=dict(default_branch="master"))
        mocker.get("https://gitlab.com/jspaaks/badge-test/-/raw/master/.howfairis.yml", status_code=404)
        return mocker


