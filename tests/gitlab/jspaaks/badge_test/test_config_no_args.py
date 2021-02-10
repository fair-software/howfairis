from howfairis import Config
from howfairis import Repo
from tests.contracts.config import Contract


def get_mocked_config():
    repo = Repo("https://gitlab.com/jspaaks/badge-test")
    return Config(repo)


class TestConfigNoArgs(Contract):

    def test_force_checklist(self, mocker):
        with mocker:
            mocked_config = get_mocked_config()
            assert mocked_config.force_checklist is None

    def test_force_citation(self, mocker):
        with mocker:
            mocked_config = get_mocked_config()
            assert mocked_config.force_citation is None

    def test_force_license(self, mocker):
        with mocker:
            mocked_config = get_mocked_config()
            assert mocked_config.force_license is None

    def test_force_registry(self, mocker):
        with mocker:
            mocked_config = get_mocked_config()
            assert mocked_config.force_registry is None

    def test_force_repository(self, mocker):
        with mocker:
            mocked_config = get_mocked_config()
            assert mocked_config.force_repository is None

    def test_include_comments(self, mocker):
        with mocker:
            mocked_config = get_mocked_config()
            assert mocked_config.include_comments is False
