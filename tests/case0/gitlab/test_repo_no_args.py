import pytest
from howfairis import Repo
from howfairis.exceptions.get_default_branch_exception import GetDefaultBranchException
from tests.contracts.repo import Contract
from tests.helpers import skip_unreachable


def get_repo():
    return Repo("https://gitlab.com/owner-doesnt-exist/repo-doesnt-exist")


class TestRepoNoArgs(Contract):

    @skip_unreachable
    def test_api(self, mocker):
        pass

    @skip_unreachable
    def test_branch(self, mocker):
        pass

    def test_default_branch(self, mocker):
        with mocker, pytest.raises(GetDefaultBranchException) as exc_info:
            get_repo()
        assert str(exc_info.value).startswith("Something went wrong asking the repo for its default branch")

    @skip_unreachable
    def test_owner(self, mocker):
        pass

    @skip_unreachable
    def test_path(self, mocker):
        pass

    @skip_unreachable
    def test_platform(self, mocker):
        pass

    @skip_unreachable
    def test_raw_url_format_string(self, mocker):
        pass

    @skip_unreachable
    def test_repo(self, mocker):
        pass

    @skip_unreachable
    def test_url(self, mocker):
        pass
