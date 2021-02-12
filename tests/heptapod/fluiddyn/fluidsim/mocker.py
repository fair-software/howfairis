import pytest
import requests_mock


@pytest.fixture
def mocker():
    """This mock aims to reflect the state of the repository at
    https://foss.heptapod.net/fluiddyn/fluidsim/-/tree/c12f0fb012a275b29076fc3baa320660dd8df2f8"""
    with requests_mock.Mocker() as m:
        m.get("https://foss.heptapod.net/fluiddyn/fluidsim")
        m.get("https://foss.heptapod.net/api/v4/projects/fluiddyn%2Ffluidsim", json=dict(default_branch="branch/default"))
        m.get("https://foss.heptapod.net/fluiddyn/fluidsim/-/raw/branch/default/.howfairis.yml", status_code=404)
        return m
