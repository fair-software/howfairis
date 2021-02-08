import pytest
import requests_mock


@pytest.fixture
def mocker():
    """This mock aims to reflect the state of the repository at
    https://gitlab.com/jspaaks/badge-test/-/tree/472713282fde87fa4c8e5116e46229c094c3c4ec"""
    with requests_mock.Mocker() as m:
        m.get("https://gitlab.com/jspaaks/badge-test")
        m.get("https://gitlab.com/api/v4/projects/jspaaks%2Fbadge-test", json=dict(default_branch="master"))
        m.get("https://gitlab.com/jspaaks/badge-test/-/raw/master/.howfairis.yml", status_code=404)
        return m
