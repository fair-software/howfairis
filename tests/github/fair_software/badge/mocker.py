import pytest
import requests_mock


@pytest.fixture
def mocker():
    """This mock aims to reflect the state of the repository at
    https://github.com/fair-software/badge/tree/b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a"""
    with requests_mock.Mocker() as mocker:
        mocker.get("http://github.com/fair-software/badge")
        mocker.get("https://api.github.com/repos/fair-software/badge", json=dict(default_branch="master"))
        mocker.get("https://raw.githubusercontent.com/fair-software/badge/master/.howfairis.yml", status_code=404)
        return mocker
