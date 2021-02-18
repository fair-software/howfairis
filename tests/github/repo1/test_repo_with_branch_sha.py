from howfairis import Platform
from howfairis import Repo
from tests.contracts.repo import Contract


def get_repo():
    return Repo("https://github.com/fair-software/badge", branch="b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a")


class TestRepoWithBranchSHA(Contract):

    def test_api(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.api == "https://api.github.com/repos/fair-software/badge"

    def test_branch(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.branch == "b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a"

    def test_default_branch(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.default_branch is None

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
            assert repo.platform == Platform.GITHUB

    def test_raw_url_format_string(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.raw_url_format_string == "https://raw.githubusercontent.com/fair-software" + \
                                                        "/badge/b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a/{0}"

    def test_repo(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.repo == "badge"

    def test_url(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.url == "https://github.com/fair-software/badge"
