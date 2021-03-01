import re
import pytest
from requests_mock import Mocker
from howfairis import Repo
from howfairis.exceptions.get_default_branch_exception import GetDefaultBranchException
from tests.contracts.repo import Contract
from tests.helpers import skip_unreachable


def get_repo():
    return Repo("https://github.com/owner-doesnt-exist/repo-doesnt-exist")


class TestRepoNoArgs(Contract):
    @skip_unreachable
    def test_api(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_branch(self, mocker: Mocker):
        pass

    def test_default_branch(self, mocker: Mocker):
        with mocker, pytest.raises(GetDefaultBranchException) as exc_info:
            get_repo()
        assert re.search("Something went wrong asking the repo for its default branch.", str(exc_info.value))

    @skip_unreachable
    def test_owner(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_path(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_platform(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_raw_url_format_string(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_repo(self, mocker: Mocker):
        pass

    @skip_unreachable
    def test_url(self, mocker: Mocker):
        pass
