from howfairis import Checker
from howfairis import Compliance
from howfairis import Config
from howfairis import Repo
from howfairis.readme import Readme
from tests.contracts.checker import Contract


def get_mocked_checker():
    repo = Repo("https://github.com/fair-software/badge")
    config = Config(repo)
    return Checker(config, repo)


class TestCheckerNoArgs(Contract):

    def test_check_checklist(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.check_checklist() is False

    def test_check_citation(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.check_citation() is True

    def test_check_license(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.check_license() is True

    def test_check_registry(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.check_registry() is True

    def test_check_repository(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.check_repository() is True

    def test_compliance(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            actual_compliance = mocked_checker.check_five_recommendations()
            expected_compliance = Compliance(True, True, True, True, False)
            assert actual_compliance == expected_compliance

    def test_config(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert isinstance(mocked_checker.config, Config)

    def test_has_ascl_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_ascl_badge() is False

    def test_has_bintray_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_bintray_badge() is False

    def test_has_citation_file(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_citation_file() is False

    def test_has_citationcff_file(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_citationcff_file() is True

    def test_has_codemeta_file(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_codemeta_file() is False

    def test_has_conda_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_conda_badge() is False

    def test_has_core_infrastructures_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_core_infrastructures_badge() is False

    def test_has_cran_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_cran_badge() is False

    def test_has_crates_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_crates_badge() is False

    def test_has_license(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_license() is True

    def test_has_maven_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_maven_badge() is False

    def test_has_npm_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_npm_badge() is False

    def test_has_open_repository(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_open_repository() is True

    def test_has_pypi_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_pypi_badge() is False

    def test_has_rsd_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_rsd_badge() is False

    def test_has_zenodo_badge(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_zenodo_badge() is False

    def test_has_zenodo_metadata_file(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.has_zenodo_metadata_file() is False

    def test_is_on_github_marketplace(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert mocked_checker.is_on_github_marketplace() is True

    def test_readme(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert isinstance(mocked_checker.readme, Readme)

    def test_repo(self, mocker):
        with mocker:
            mocked_checker = get_mocked_checker()
            assert isinstance(mocked_checker.repo, Repo)
