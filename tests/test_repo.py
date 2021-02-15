from requests_mock import Mocker
from howfairis import Repo
from howfairis.code_repository_platforms import Platform


def test_github_platform(requests_mock: Mocker):
    requests_mock.get("https://api.github.com/repos/fair-software/howfairis", json={"default_branch": "master"} )

    repo = Repo("https://github.com/fair-software/howfairis")
    assert repo.platform == Platform.GITHUB, "platform not GitHub"
