from click.testing import CliRunner
from requests_mock import Mocker
from howfairis.cli.cli import cli


def test_matching_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    filename = "README.rst"
    url = "https://github.com/{0}/{1}".format(owner, repo_string)
    api = "https://api.github.com/repos/{0}/{1}".format(owner, repo_string)
    raw = "https://raw.githubusercontent.com/{0}/{1}/main".format(owner, repo_string)
    reuse_url = "https://api.reuse.software/status/github.com/{0}/{1}.json".format(
        owner, repo_string
    )
    howfairis_badge = "https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green"
    pypi_badge = "https://img.shields.io/pypi/v/howfairis.svg?colorB=blue"
    cii_badge = "https://bestpractices.coreinfrastructure.org/projects/4630/badge"
    requests_mock.get(url, status_code=200)
    requests_mock.get(api, json={"default_branch": "main"}, status_code=200)
    requests_mock.get(api + "/license", status_code=200)
    requests_mock.get(raw + "/.howfairis.yml", status_code=200)
    requests_mock.get(raw + "/CITATION", status_code=200)
    requests_mock.get(raw + "/CITATION.cff", status_code=200)
    requests_mock.get(raw + "/codemeta.json", status_code=200)
    requests_mock.get(
        raw + "/" + filename,
        text=howfairis_badge + pypi_badge + cii_badge,
        status_code=200,
    )
    requests_mock.get(raw + "/.zenodo.json", status_code=200)
    requests_mock.get(api + "/commits", json=[], status_code=200)
    reuse_return_value = {"error": "Not a Git repository"}
    requests_mock.get(reuse_url, json=reuse_return_value, status_code=400)

    runner = CliRunner()
    response = runner.invoke(cli, [url])
    assert response.exit_code == 0


def test_upgraded_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    filename = "README.rst"
    url = "https://github.com/{0}/{1}".format(owner, repo_string)
    api = "https://api.github.com/repos/{0}/{1}".format(owner, repo_string)
    raw = "https://raw.githubusercontent.com/{0}/{1}/main".format(owner, repo_string)
    howfairis_badge = "https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow"
    pypi_badge = "https://img.shields.io/pypi/v/howfairis.svg?colorB=blue"
    cii_badge = "https://bestpractices.coreinfrastructure.org/projects/4630/badge"
    requests_mock.get(url, status_code=200)
    requests_mock.get(api, json={"default_branch": "main"}, status_code=200)
    requests_mock.get(api + "/license", status_code=200)
    requests_mock.get(raw + "/.howfairis.yml", status_code=200)
    requests_mock.get(raw + "/CITATION", status_code=200)
    requests_mock.get(raw + "/CITATION.cff", status_code=200)
    requests_mock.get(raw + "/codemeta.json", status_code=200)
    requests_mock.get(
        raw + "/" + filename,
        text=howfairis_badge + pypi_badge + cii_badge,
        status_code=200,
    )
    requests_mock.get(raw + "/.zenodo.json", status_code=200)
    requests_mock.get(api + "/commits", json=[], status_code=200)
    runner = CliRunner()
    response = runner.invoke(cli, [url])
    assert response.exit_code == 1


def test_mismatching_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    filename = "README.rst"
    url = "https://github.com/{0}/{1}".format(owner, repo_string)
    api = "https://api.github.com/repos/{0}/{1}".format(owner, repo_string)
    raw = "https://raw.githubusercontent.com/{0}/{1}/main".format(owner, repo_string)
    howfairis_badge = "https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green"
    requests_mock.get(url, status_code=200)
    requests_mock.get(api, json={"default_branch": "main"}, status_code=200)
    requests_mock.get(api + "/license", status_code=200)
    requests_mock.get(raw + "/.howfairis.yml", status_code=200)
    requests_mock.get(raw + "/CITATION", status_code=200)
    requests_mock.get(raw + "/CITATION.cff", status_code=200)
    requests_mock.get(raw + "/codemeta.json", status_code=200)
    requests_mock.get(raw + "/" + filename, text=howfairis_badge, status_code=200)
    requests_mock.get(raw + "/.zenodo.json", status_code=200)
    requests_mock.get(api + "/commits", json=[], status_code=200)
    runner = CliRunner()
    response = runner.invoke(cli, [url])
    assert response.exit_code == 1


def test_missing_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    filename = "README.rst"
    url = "https://github.com/{0}/{1}".format(owner, repo_string)
    api = "https://api.github.com/repos/{0}/{1}".format(owner, repo_string)
    raw = "https://raw.githubusercontent.com/{0}/{1}/main".format(owner, repo_string)
    requests_mock.get(url, status_code=200)
    requests_mock.get(api, json={"default_branch": "main"}, status_code=200)
    requests_mock.get(api + "/license", status_code=200)
    requests_mock.get(raw + "/.howfairis.yml", status_code=200)
    requests_mock.get(raw + "/CITATION", status_code=200)
    requests_mock.get(raw + "/CITATION.cff", status_code=200)
    requests_mock.get(raw + "/codemeta.json", status_code=200)
    requests_mock.get(raw + "/" + filename, text="", status_code=200)
    requests_mock.get(raw + "/.zenodo.json", status_code=200)
    requests_mock.get(api + "/commits", json=[], status_code=200)
    runner = CliRunner()
    response = runner.invoke(cli, [url])
    assert response.exit_code == 1
