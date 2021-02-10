from howfairis import Platform
from howfairis import Repo
from tests.contracts.repo import Contract


def get_mocked_repo():
    return Repo("https://github.com/fair-software/badge", path="mypath")


class TestRepoNoArgs(Contract):

    def test_api(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.api == "https://api.github.com/repos/fair-software/badge"

    def test_branch(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.branch is None

    def test_config_file(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.config_file is None

    def test_default_branch(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.default_branch == "master"

    def test_owner(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.owner == "fair-software"

    def test_path(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.path == "/mypath"

    def test_platform(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.platform == Platform.GITHUB

    def test_raw_url_format_string(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.raw_url_format_string == "https://raw.githubusercontent.com/fair-software" + \
                                                        "/badge/master/mypath/{0}"

    def test_repo(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.repo == "badge"

    def test_url(self, mocker):
        with mocker:
            mocked_repo = get_mocked_repo()
            assert mocked_repo.url == "https://github.com/fair-software/badge"
