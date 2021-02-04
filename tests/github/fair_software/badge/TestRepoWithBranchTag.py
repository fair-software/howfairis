from tests.contracts.Repo import Contract
import pytest
from tests.github.fair_software.badge.mocker import mocker
from howfairis import Platform
from howfairis import Repo


@pytest.fixture
def mocked_repo(mocker):
    with mocker:
        return Repo("https://github.com/fair-software/badge", branch="0.1.0")


class TestRepoWithBranchTag(Contract):

    def test_api(self, mocked_repo):
        assert mocked_repo.api == "https://api.github.com/repos/fair-software/badge"

    def test_branch(self, mocked_repo):
        assert mocked_repo.branch == "0.1.0"

    def test_config_file(self, mocked_repo):
        assert mocked_repo.config_file is None

    def test_default_branch(self, mocked_repo):
        assert mocked_repo.default_branch == "master"

    def test_owner(self, mocked_repo):
        assert mocked_repo.owner == "fair-software"

    def test_path(self, mocked_repo):
        assert mocked_repo.path == ""

    def test_platform(self, mocked_repo):
        assert mocked_repo.platform == Platform.GITHUB

    def test_raw_url_format_string(self, mocked_repo):
        assert mocked_repo.raw_url_format_string == "https://raw.githubusercontent.com/fair-software" + \
                                                         "/badge/0.1.0/{0}"

    def test_repo(self, mocked_repo):
        assert mocked_repo.repo == "badge"

    def test_url(self, mocked_repo):
        assert mocked_repo.url == "https://github.com/fair-software/badge"
