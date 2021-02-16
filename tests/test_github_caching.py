from datetime import datetime
from datetime import timedelta
from dateutil import tz
from requests_mock import Mocker
from howfairis.checker import Checker
from howfairis.repo import Repo
from howfairis.workarounds.github_caching import github_caching_check


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
    repo = Repo(url, branch="main")
    checker = Checker(repo)
    capsys.readouterr()
    github_caching_check(checker)
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
    repo = Repo(url, branch="main")
    checker = Checker(repo)
    capsys.readouterr()
    github_caching_check(checker)
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
    repo = Repo(url, branch="main")
    checker = Checker(repo)
    capsys.readouterr()
    github_caching_check(checker)
    actual_out_err = capsys.readouterr()
    expected_out = ""
    assert actual_out_err[0] == expected_out
