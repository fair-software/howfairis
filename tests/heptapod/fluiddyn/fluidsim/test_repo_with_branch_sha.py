import pytest
from howfairis import Platform
from howfairis import Repo
from tests.contracts.repo import Contract
from .mocker import mocker


@pytest.fixture
def mocked_repo(mocker):
    with mocker:
        return Repo("https://foss.heptapod.net/fluiddyn/fluidsim", branch="b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a")


class TestRepoWithBranchSHA(Contract):

    def test_api(self, mocked_repo):
        assert mocked_repo.api == "https://foss.heptapod.net/api/v4/projects/fluiddyn%2Ffluidsim"

    def test_branch(self, mocked_repo):
        assert mocked_repo.branch == "b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a"

    def test_default_branch(self, mocked_repo):
        assert mocked_repo.default_branch == "branch/default"

    def test_owner(self, mocked_repo):
        assert mocked_repo.owner == "fluiddyn"

    def test_path(self, mocked_repo):
        assert mocked_repo.path == ""

    def test_platform(self, mocked_repo):
        assert mocked_repo.platform == Platform.HEPTAPOD

    def test_raw_url_format_string(self, mocked_repo):
        assert mocked_repo.raw_url_format_string == \
            "https://foss.heptapod.net/fluiddyn/fluidsim/-/raw/b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a/{0}"

    def test_repo(self, mocked_repo):
        assert mocked_repo.repo == "fluidsim"

    def test_url(self, mocked_repo):
        assert mocked_repo.url == "https://foss.heptapod.net/fluiddyn/fluidsim"
