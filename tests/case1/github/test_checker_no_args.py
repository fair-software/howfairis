from howfairis import Checker
from howfairis import Compliance
from howfairis import Repo
from howfairis.readme import Readme
from tests.contracts.checker import Contract


def get_checker():
    repo = Repo("https://github.com/fair-software/repo1")
    return Checker(repo)


class TestCheckerNoArgs(Contract):

    def test_check_checklist(self, mocker, capsys):
        with mocker:
            checker = get_checker()
            assert checker.check_checklist() is False

    def test_check_citation(self, mocker, capsys):
        with mocker:
            checker = get_checker()
            assert checker.check_citation() is False

    def test_check_license(self, mocker, capsys):
        with mocker:
            checker = get_checker()
            assert checker.check_license() is True

    def test_check_registry(self, mocker, capsys):
        with mocker:
            checker = get_checker()
            assert checker.check_registry() is True

    def test_check_repository(self, mocker, capsys):
        with mocker:
            checker = get_checker()
            assert checker.check_repository() is True

    def test_compliance(self, mocker):
        with mocker:
            checker = get_checker()
            actual_compliance = checker.check_five_recommendations()
            expected_compliance = Compliance(True, True, True, False, False)
            assert actual_compliance == expected_compliance

    def test_has_ascl_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_ascl_badge() is False

    def test_has_bintray_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_bintray_badge() is False

    def test_has_citation_file(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_citation_file() is False

    def test_has_citationcff_file(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_citationcff_file() is False

    def test_has_codemeta_file(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_codemeta_file() is False

    def test_has_conan_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_conan_badge() is False

    def test_has_conda_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_conda_badge() is False

    def test_has_core_infrastructures_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_core_infrastructures_badge() is False

    def test_has_cran_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_cran_badge() is False

    def test_has_crates_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_crates_badge() is False

    def test_has_license(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_license() is True

    def test_has_maven_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_maven_badge() is False

    def test_has_npm_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_npm_badge() is False

    def test_has_open_repository(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_open_repository() is True

    def test_has_pypi_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_pypi_badge() is False

    def test_has_rsd_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_rsd_badge() is False

    def test_has_zenodo_badge(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_zenodo_badge() is False

    def test_has_zenodo_metadata_file(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.has_zenodo_metadata_file() is False

    def test_is_on_github_marketplace(self, mocker):
        with mocker:
            checker = get_checker()
            assert checker.is_on_github_marketplace() is True

    def test_readme(self, mocker):
        with mocker:
            checker = get_checker()
            assert isinstance(checker.readme, Readme)

    def test_repo(self, mocker):
        with mocker:
            checker = get_checker()
            assert isinstance(checker.repo, Repo)
