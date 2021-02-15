from datetime import datetime
from datetime import timedelta
import pytest
from dateutil import tz
from requests_mock import Mocker
from howfairis import Checker
from howfairis import Compliance
from howfairis import Repo
from howfairis.readme import Readme


@pytest.fixture
def badghurl_checker(requests_mock: Mocker):
    requests_mock.get("https://raw.githubusercontent.com/fair-software/does-not-exist/main/.howfairis.yml", status_code=404)
    requests_mock.get("https://raw.githubusercontent.com/fair-software/does-not-exist/main/.howfairis.yml", status_code=404)
    requests_mock.get("https://raw.githubusercontent.com/fair-software/does-not-exist/main/README.md", status_code=404)
    requests_mock.get("https://raw.githubusercontent.com/fair-software/does-not-exist/main/README.rst", status_code=404)
    requests_mock.get("https://api.github.com/repos/fair-software/does-not-exist", status_code=404)
    requests_mock.get("https://api.github.com/repos/fair-software/does-not-exist/license", status_code=404)
    requests_mock.get("https://github.com/fair-software/does-not-exist", status_code=404)
    requests_mock.get("https://raw.githubusercontent.com/fair-software/does-not-exist/main/CITATION", status_code=404)
    requests_mock.get("https://raw.githubusercontent.com/fair-software/does-not-exist/main/CITATION.cff", status_code=404)
    requests_mock.get("https://raw.githubusercontent.com/fair-software/does-not-exist/main/codemeta.json", status_code=404)
    requests_mock.get("https://raw.githubusercontent.com/fair-software/does-not-exist/main/.zenodo.json", status_code=404)

    repo = Repo("https://github.com/fair-software/does-not-exist")
    checker = Checker(repo)
    return checker


def test_checker_badghurl_emptyreadme(badghurl_checker: Checker):
    actual_readme = badghurl_checker.readme

    expected_readme = Readme(filename=None, text=None, file_format=None)
    assert actual_readme == expected_readme


def test_checker_check_five_recommendations(badghurl_checker: Checker):
    actual_compliance = badghurl_checker.check_five_recommendations()

    expected_compliance = Compliance(repository=False, license_=False, registry=False, citation=False, checklist=False)
    assert actual_compliance == expected_compliance


def test_github_readme_creation_check_critical_time(requests_mock: Mocker, capsys):
    owner = "fair-software"
    repo_string = "howfairis"
    filename = "README.rst"
    url = f"https://github.com/{owner}/{repo_string}"
    date_now = datetime.now().astimezone(tz.tzutc())
    date_now_string = date_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}",
                      json={"created_at": date_now_string}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/main/{filename}",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/main/.howfairis.yml",
                      json={}, status_code=200)
    repo = Repo(url)
    checker = Checker(repo)
    capsys.readouterr()
    checker.github_readme_creation_check()
    actual_out_err = capsys.readouterr()
    expected_out = (f"Warning: Your {filename} was updated less than 5 minutes ago. " +
                    "The effects of this update are not visible yet in the calculated compliance.\n")
    assert actual_out_err[0] == expected_out


def test_github_readme_creation_check_fine_time(requests_mock: Mocker, capsys):
    owner = "fair-software"
    repo_string = "howfairis"
    filename = "README.rst"
    url = f"https://github.com/{owner}/{repo_string}"
    date_now = datetime.now().astimezone(tz.tzutc())
    date_past_string = (date_now-timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    requests_mock.get(f"https://api.github.com/repos/{owner}/{repo_string}",
                      json={"created_at": date_past_string}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/main/{filename}",
                      json={}, status_code=200)
    requests_mock.get(f"https://raw.githubusercontent.com/{owner}/{repo_string}/main/.howfairis.yml",
                      json={}, status_code=200)
    repo = Repo(url)
    checker = Checker(repo)
    capsys.readouterr()
    checker.github_readme_creation_check()
    actual_out_err = capsys.readouterr()
    expected_out = ""
    assert actual_out_err[0] == expected_out


def test_github_readme_creation_check_no_time(requests_mock: Mocker, capsys):
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
    repo = Repo(url)
    checker = Checker(repo)
    capsys.readouterr()
    checker.github_readme_creation_check()
    actual_out_err = capsys.readouterr()
    expected_out = ""
    assert actual_out_err[0] == expected_out
