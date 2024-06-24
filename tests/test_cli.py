import os
from click.testing import CliRunner
from requests_mock import Mocker
from howfairis import Compliance
from howfairis.cli.cli import cli
from howfairis.cli.print_call_to_action import automate_call_to_action

def test_matching_badge(requests_mock: Mocker):
    owner = "fair-software"
    repo_string = "howfairis"
    filename = "README.rst"
    url = "https://github.com/{0}/{1}".format(owner, repo_string)
    api = "https://api.github.com/repos/{0}/{1}".format(owner, repo_string)
    raw = "https://raw.githubusercontent.com/{0}/{1}/main".format(owner, repo_string)
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
    requests_mock.get(raw + "/" + filename, text=howfairis_badge+pypi_badge+cii_badge, status_code=200)
    requests_mock.get(raw + "/.zenodo.json", status_code=200)
    requests_mock.get(api + "/commits", json=[], status_code=200)
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
    requests_mock.get(raw + "/" + filename, text=howfairis_badge+pypi_badge+cii_badge, status_code=200)
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


def test_automate_call_to_action():

    test_filename = "test-automate-call-to-action--readme.md"

    # Mock the Checker
    class Repo:
        platform = "test"
    class Readme:
        filename = test_filename
        text = 1
    class Checker:
        readme = Readme
        repo = Repo

    previous_compliance = Compliance(False, False, False, False, False)
    current_compliance = Compliance(False, False, False, False, True)

    try:
        test_README_string = previous_compliance.badge_image_url()
        with open(test_filename, "w") as test_file:
            test_file.write(test_README_string)

        automate_call_to_action(previous_compliance, current_compliance, Checker)

        with open(test_filename, "r") as test_file:
            result = test_file.read()
        assert result == current_compliance.badge_image_url()

    finally:
        # cleanup the temporary file test_filename
        try:
            os.remove(test_filename)
        except OSError as e:
            # if the file does not exist, ignore the exception
            if e.errno != errno.ENOENT:
                raise e


