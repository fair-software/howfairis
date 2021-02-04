from tests.contracts.Repo import Contract
import unittest
import pytest
from tests.github.fair_software.badge.mocks import mocker
from howfairis import Platform
from howfairis import Repo


@pytest.fixture
def mocked_repo(mocker):
    with mocker:
        return Repo("https://github.com/fair-software/badge")


class TestRepoNoArgs(Contract, unittest.TestCase):

    @pytest.fixture(autouse=True)
    def __inject_fixtures(self, mocked_repo):
        self.mocked_repo = mocked_repo

    def test_api(self):
        assert self.mocked_repo.api == "https://api.github.com/repos/fair-software/badge"

    def test_branch(self):
        assert self.mocked_repo.branch is None

    def test_config_file(self):
        assert self.mocked_repo.config_file is None

    def test_default_branch(self):
        assert self.mocked_repo.default_branch == "master"

    def test_owner(self):
        assert self.mocked_repo.owner == "fair-software"

    def test_path(self):
        assert self.mocked_repo.path == ""

    def test_platform(self):
        assert self.mocked_repo.platform == Platform.GITHUB

    def test_raw_url_format_string(self):
        assert self.mocked_repo.raw_url_format_string == "https://raw.githubusercontent.com/fair-software" + \
                                                         "/badge/master/{0}"

    def test_repo(self):
        assert self.mocked_repo.repo == "badge"

    def test_url(self):
        assert self.mocked_repo.url == "https://github.com/fair-software/badge"
