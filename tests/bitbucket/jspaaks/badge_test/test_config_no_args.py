import pytest
from howfairis import Config
from howfairis import Repo
from tests.contracts.config import Contract
from .mocker import mocker


@pytest.fixture
def mocked_config(mocker):
    with mocker:
        repo = Repo("https://bitbucket.org/jspaaks/badge-test")
        return Config(repo)


class TestConfigNoArgs(Contract):

    def test_force_checklist(self, mocked_config):
        assert mocked_config.force_checklist is None

    def test_force_citation(self, mocked_config):
        assert mocked_config.force_citation is None

    def test_force_license(self, mocked_config):
        assert mocked_config.force_license is None

    def test_force_registry(self, mocked_config):
        assert mocked_config.force_registry is None

    def test_force_repository(self, mocked_config):
        assert mocked_config.force_repository is None

    def test_include_comments(self, mocked_config):
        assert mocked_config.include_comments is False

