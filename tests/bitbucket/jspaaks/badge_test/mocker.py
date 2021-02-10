import pytest
import requests_mock


@pytest.fixture
def mocker():
    with requests_mock.Mocker() as m:
        default_branch_json = {
            "mainbranch": {
                "type": "branch",
                "name": "master"
            }
        }
        m.get("http://bitbucket.org/jspaaks/badge-test")
        m.get("https://api.bitbucket.org/2.0/repositories/jspaaks/badge-test", json=default_branch_json)
        m.get("https://bitbucket.org/jspaaks/badge-test/raw/master/.howfairis.yml", status_code=404)
        m.get("https://bitbucket.org/jspaaks/badge-test/raw/e87814ff014115bb07dbd84e44daee104132113e/.howfairis.yml",
              status_code=404)
        m.get("https://bitbucket.org/jspaaks/badge-test/raw/0.1.0/.howfairis.yml", status_code=404)
        m.get("https://bitbucket.org/jspaaks/badge-test/raw/master/.howfairis-custom-config.yml", status_code=404)

        return m
