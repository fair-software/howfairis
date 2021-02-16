from datetime import datetime
from datetime import timedelta
import pytest
from dateutil import tz
from requests_mock import Mocker
from howfairis import Checker
from howfairis import Compliance
from howfairis import Repo
from howfairis.cli import cli


def test_matching_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    filename = "README.rst"
    url = f"https://github.com/{owner}/{repo_string}"
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/main/{filename}",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/main/.howfairis.yml",
                      json={}, status_code=200)
    actual_exit_code = cli(url,None)
    expected_exit_code = 0
    assert actual_exit_code == expected_exit_code
