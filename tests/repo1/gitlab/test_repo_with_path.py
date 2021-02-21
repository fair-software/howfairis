from howfairis import Platform
from howfairis import Repo
from tests.contracts.repo import Contract


def get_repo():
    return Repo("https://gitlab.com/owner1/repo1", path="mypath")


class TestRepoWithPath(Contract):

    def test_api(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.api == "https://gitlab.com/api/v4/projects/owner1%2Frepo1"

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
            assert repo.owner == "owner1"

    def test_path(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.path == "/mypath"

    def test_platform(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.platform == Platform.GITLAB

    def test_raw_url_format_string(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.raw_url_format_string == "https://gitlab.com/owner1/repo1/-/raw/master/mypath/{0}"

    def test_repo(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.repo == "repo1"

    def test_url(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.url == "https://gitlab.com/owner1/repo1"