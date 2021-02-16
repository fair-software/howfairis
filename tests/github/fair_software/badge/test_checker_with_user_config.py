import pytest
from requests_mock import Mocker
from howfairis import Checker
from howfairis import Repo
from tests.contracts.checker import Contract


def get_mocked_checker(user_config_filename):
    repo = Repo("https://github.com/fair-software/badge")
    return Checker(repo, user_config_filename=user_config_filename)


@pytest.fixture
def user_config(tmp_path):
    config = tmp_path / "howfairis.yml"
    text = """skip_repository_checks_reason: dunno1
skip_license_checks_reason: dunno2
skip_registry_checks_reason: dunno3
skip_citation_checks_reason: dunno4
skip_checklist_checks_reason: dunno5    
"""
    config.write_text(text)
    yield config


class TestCheckerWithUserConfig(Contract):
    def test_check_checklist(self, mocker: Mocker, user_config, capsys):
        with mocker:
            checker = get_mocked_checker(user_config)
            assert checker.check_checklist() is True
            captured = capsys.readouterr()
            assert "dunno5" in captured.out

    def test_check_citation(self, mocker: Mocker, user_config, capsys):
        with mocker:
            checker = get_mocked_checker(user_config)
            assert checker.check_citation() is True
            captured = capsys.readouterr()
            assert "dunno4" in captured.out

    def test_check_license(self, mocker: Mocker, user_config, capsys):
        with mocker:
            checker = get_mocked_checker(user_config)
            assert checker.check_license() is True
            captured = capsys.readouterr()
            assert "dunno2" in captured.out

    def test_check_registry(self, mocker: Mocker, user_config, capsys):
        with mocker:
            checker = get_mocked_checker(user_config)
            assert checker.check_registry() is True
            captured = capsys.readouterr()
            assert "dunno3" in captured.out

    def test_check_repository(self, mocker: Mocker, user_config, capsys):
        with mocker:
            checker = get_mocked_checker(user_config)
            assert checker.check_repository() is True
            captured = capsys.readouterr()
            assert "dunno1" in captured.out

    def test_compliance(self, mocker: Mocker):
        pass

    def test_has_ascl_badge(self, mocker: Mocker):
        pass

    def test_has_bintray_badge(self, mocker: Mocker):
        pass

    def test_has_citation_file(self, mocker: Mocker):
        pass

    def test_has_citationcff_file(self, mocker: Mocker):
        pass

    def test_has_codemeta_file(self, mocker: Mocker):
        pass

    def test_has_conda_badge(self, mocker: Mocker):
        pass

    def test_has_core_infrastructures_badge(self, mocker: Mocker):
        pass

    def test_has_cran_badge(self, mocker: Mocker):
        pass

    def test_has_crates_badge(self, mocker: Mocker):
        pass

    def test_has_license(self, mocker: Mocker):
        pass

    def test_has_maven_badge(self, mocker: Mocker):
        pass

    def test_has_npm_badge(self, mocker: Mocker):
        pass

    def test_has_open_repository(self, mocker: Mocker):
        pass

    def test_has_pypi_badge(self, mocker: Mocker):
        pass

    def test_has_rsd_badge(self, mocker: Mocker):
        pass

    def test_has_zenodo_badge(self, mocker: Mocker):
        pass

    def test_has_zenodo_metadata_file(self, mocker: Mocker):
        pass

    def test_is_on_github_marketplace(self, mocker: Mocker):
        pass

    def test_readme(self, mocker: Mocker):
        pass

    def test_repo(self, mocker: Mocker):
        pass
