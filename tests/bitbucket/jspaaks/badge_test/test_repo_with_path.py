import pytest
from howfairis import Platform
from howfairis import Repo
from tests.contracts.repo import Contract
from .mocker import mocker


@pytest.fixture
def mocked_repo(mocker):
    with mocker:
        return Repo("https://bitbucket.org/jspaaks/badge-test", path="mypath")


class TestRepoWithPath(Contract):

    def test_api(self, mocked_repo):
        assert mocked_repo.api == "https://api.bitbucket.org/2.0/repositories/jspaaks/badge-test"

    def test_branch(self, mocked_repo):
        assert mocked_repo.branch is None

    def test_config_file(self, mocked_repo):
        assert mocked_repo.config_file is None

    def test_default_branch(self, mocked_repo):
        assert mocked_repo.default_branch == "master"

    def test_owner(self, mocked_repo):
        assert mocked_repo.owner == "jspaaks"

    def test_path(self, mocked_repo):
        assert mocked_repo.path == "/mypath"

    def test_platform(self, mocked_repo):
        assert mocked_repo.platform == Platform.BITBUCKET

    def test_raw_url_format_string(self, mocked_repo):
        assert mocked_repo.raw_url_format_string == "https://bitbucket.org/jspaaks/badge-test/raw/master/mypath/{0}"

    def test_repo(self, mocked_repo):
        assert mocked_repo.repo == "badge-test"

    def test_url(self, mocked_repo):
        assert mocked_repo.url == "https://bitbucket.org/jspaaks/badge-test"
