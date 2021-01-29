from howfairis import Repo
from howfairis.Platform import Platform


def test_github_platform():
    repo = Repo('https://github.com/fair-software/does-not-exist')
    assert repo.platform == Platform.GITHUB, 'platform not GitHub'
