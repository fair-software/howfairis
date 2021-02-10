from datetime import datetime
from datetime import timedelta
from dateutil import tz
from requests_mock import Mocker
from howfairis.cli import github_readme_creation_check
from howfairis.vcs_platform import Platform


def test_github_readme_creation_check_platform():
    actual_return_code = github_readme_creation_check("", "", Platform.GITLAB, None)
    expected_return_code = 0
    assert actual_return_code == expected_return_code


def test_github_readme_creation_check_critical_time(requests_mock: Mocker):
    url = "https://github.com/fair-software/howfairis"
    filename = "README.rst"
    platform = Platform.GITHUB
    branch = None
    date_now = datetime.now().astimezone(tz.tzutc())
    date_string = date_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    requests_mock.get(url+"/blob/master/"+filename,
                      text=f'<relative-time datetime="{date_string}">')
    actual_return_code = github_readme_creation_check(url, filename, platform, branch)
    expected_return_code = 1
    assert actual_return_code == expected_return_code


def test_github_readme_creation_check_fine_time(requests_mock: Mocker):
    url = "https://github.com/fair-software/howfairis"
    filename = "README.rst"
    platform = Platform.GITHUB
    branch = None
    date_now = datetime.now().astimezone(tz.tzutc())
    date_string = (date_now-timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    requests_mock.get(url+"/blob/master/"+filename,
                      text=f'<relative-time datetime="{date_string}">')
    actual_return_code = github_readme_creation_check(url, filename, platform, branch)
    expected_return_code = 0
    assert actual_return_code == expected_return_code


def test_github_readme_creation_check_no_times_available(requests_mock: Mocker):
    url = "https://github.com/fair-software/howfairis"
    filename = "README.rst"
    platform = Platform.GITHUB
    branch = "master"
    requests_mock.get(url+"/blob/master/"+filename, text="there is no time here")
    requests_mock.get(url+"/contributors/master/"+filename, text="there is no time here")
    actual_return_code = github_readme_creation_check(url, filename, platform, branch)
    expected_return_code = 0
    assert actual_return_code == expected_return_code
