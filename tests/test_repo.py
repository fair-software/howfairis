from requests_mock import Mocker

from howfairis import Repo
from howfairis.code_repository_platforms import Platform


def test_notfound_url(requests_mock: Mocker):
    requests_mock.get('https://api.github.com/repos/fair-software/does-not-exist', status_code=404)

    repo = Repo('https://github.com/fair-software/does-not-exist')
    assert repo.platform == Platform.GITHUB, 'platform not GitHub'


def test_github_platform(requests_mock: Mocker):
    requests_mock.get('https://api.github.com/repos/fair-software/howfairis', json={'default_branch': 'master'} )

    repo = Repo('https://github.com/fair-software/howfairis')
    assert repo.platform == Platform.GITHUB, 'platform not GitHub'
