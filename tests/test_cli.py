import re
from datetime import datetime
from datetime import timedelta
from click.testing import CliRunner
from dateutil import tz
from requests_mock import Mocker
from howfairis.checker import Checker
from howfairis.cli import cli
from howfairis.repo import Repo


runner = CliRunner()


def test_invalid_url():
    runner = CliRunner()
    response = runner.invoke(cli, [""])
    expected_message = "url should start with https://"
    assert response.exception.args[0] == expected_message


def test_url_not_git():
    runner = CliRunner()
    response = runner.invoke(cli, ["https://www.esciencecenter.nl"])
    expected_message = "Repository should be on github.com or on gitlab.com."
    assert response.exception.args[0] == expected_message


def test_url_not_repository():
    runner = CliRunner()
    response = runner.invoke(cli, ["https://github.com/fair-software"])
    expected_message = "url is not a repository"
    assert response.exception.args[0] == expected_message


def test_matching_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    url = f"https://github.com/{owner}/{repo_string}"
    howfairis_badge = "https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green"
    pypi_badge = "https://img.shields.io/pypi/v/howfairis.svg?colorB=blue"
    cii_badge = "https://bestpractices.coreinfrastructure.org/projects/4630/badge"
    requests_mock.get(url,
                      text="", status_code=200)
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}",
                      json={"default_branch": "master"}, status_code=200)
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}/license",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/.howfairis.yml",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/CITATION",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/CITATION.cff",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/codemeta.json",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/README.rst",
                      text=howfairis_badge+pypi_badge+cii_badge, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/.zenodo.json",
                      json={}, status_code=200)
    repo = Repo(url)
    checker = Checker(repo)
    date_critical_utc = datetime.now().replace(second=0).astimezone(tz.tzutc()) - timedelta(minutes=5)
    date_critical_utc_string = date_critical_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    requests_mock.get(f"{checker.repo.api}/commits?page=0&per_page=1&" +
                      "path={checker.readme.filename}&since=" + date_critical_utc_string,
                      text="", status_code=200)
    runner = CliRunner()
    response = runner.invoke(cli, [url])
    expected_exit_code = 0
    expected_output = "all good"
    assert response.exit_code == expected_exit_code and re.search(expected_output, response.output)


def test_upgraded_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    url = f"https://github.com/{owner}/{repo_string}"
    howfairis_badge = "https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-green"
    pypi_badge = "https://img.shields.io/pypi/v/howfairis.svg?colorB=blue"
    cii_badge = "https://bestpractices.coreinfrastructure.org/projects/4630/badge"
    requests_mock.get(url,
                      text="", status_code=200)
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}",
                      json={"default_branch": "master"}, status_code=200)
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}/license",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/.howfairis.yml",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/CITATION",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/CITATION.cff",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/codemeta.json",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/README.rst",
                      text=howfairis_badge+pypi_badge+cii_badge, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/.zenodo.json",
                      json={}, status_code=200)
    repo = Repo(url)
    checker = Checker(repo)
    date_critical_utc = datetime.now().replace(second=0).astimezone(tz.tzutc()) - timedelta(minutes=5)
    date_critical_utc_string = date_critical_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    requests_mock.get(f"{checker.repo.api}/commits?page=0&per_page=1&" +
                      "path={checker.readme.filename}&since=" + date_critical_utc_string,
                      text="", status_code=200)
    runner = CliRunner()
    response = runner.invoke(cli, [url])
    expected_exit_code = 1
    expected_output = "Congratulations"
    assert response.exit_code == expected_exit_code and re.search(expected_output, response.output)


def test_mismatching_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    url = f"https://github.com/{owner}/{repo_string}"
    howfairis_badge = "https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green"
    requests_mock.get(url,
                      text="", status_code=200)
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}",
                      json={"default_branch": "master"}, status_code=200)
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}/license",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/.howfairis.yml",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/CITATION",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/CITATION.cff",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/codemeta.json",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/README.rst",
                      text=howfairis_badge, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/.zenodo.json",
                      json={}, status_code=200)
    repo = Repo(url)
    checker = Checker(repo)
    date_critical_utc = datetime.now().replace(second=0).astimezone(tz.tzutc()) - timedelta(minutes=5)
    date_critical_utc_string = date_critical_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    requests_mock.get(f"{checker.repo.api}/commits?page=0&per_page=1&" +
                      "path={checker.readme.filename}&since=" + date_critical_utc_string,
                      text="", status_code=200)
    runner = CliRunner()
    response = runner.invoke(cli, [url])
    expected_exit_code = 1
    expected_output = "different from"
    assert response.exit_code == expected_exit_code and re.search(expected_output, response.output)


def test_missing_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    url = f"https://github.com/{owner}/{repo_string}"
    requests_mock.get(url,
                      text="", status_code=200)
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}",
                      json={"default_branch": "master"}, status_code=200)
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}/license",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/.howfairis.yml",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/CITATION",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/CITATION.cff",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/codemeta.json",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/README.rst",
                      text="", status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/master/.zenodo.json",
                      json={}, status_code=200)
    repo = Repo(url)
    checker = Checker(repo)
    date_critical_utc = datetime.now().replace(second=0).astimezone(tz.tzutc()) - timedelta(minutes=5)
    date_critical_utc_string = date_critical_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    requests_mock.get(f"{checker.repo.api}/commits?page=0&per_page=1&" +
                      "path={checker.readme.filename}&since=" + date_critical_utc_string,
                      text="", status_code=200)
    runner = CliRunner()
    response = runner.invoke(cli, [url])
    expected_exit_code = 1
    expected_output = "It seems"
    assert response.exit_code == expected_exit_code and re.search(expected_output, response.output)
