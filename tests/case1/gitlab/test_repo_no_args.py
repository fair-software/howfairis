from howfairis import Platform
from howfairis import Repo
from tests.contracts.repo import Contract


def get_repo():
    return Repo("https://gitlab.com/fair-software/repo1")


class TestRepoNoArgs(Contract):

    def test_api(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.api == "https://gitlab.com/api/v4/projects/fair-software%2Frepo1"

    def test_branch(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.branch is None

    def test_default_branch(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.default_branch == "master"

    def test_owner(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.owner == "fair-software"

    def test_path(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.path == ""

    def test_platform(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.platform == Platform.GITLAB

    def test_raw_url_format_string(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.raw_url_format_string == "https://gitlab.com/fair-software/repo1/-/raw/master/{0}"

    def test_repo(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.repo == "repo1"

    def test_url(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.url == "https://gitlab.com/fair-software/repo1"
