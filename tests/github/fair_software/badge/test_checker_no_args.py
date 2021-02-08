import pytest
from howfairis import Checker
from howfairis import Config
from howfairis import Repo
from tests.contracts.checker import Contract
from .mocker import mocker


@pytest.fixture
def mocked_checker(mocker):
    with mocker:
        repo = Repo("https://github.com/fair-software/badge")
        config = Config(repo)
        return Checker(config, repo)


class TestCheckerNoArgs(Contract):

    @pytest.mark.skip
    def test_check_checklist(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_check_citation(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_check_license(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_check_registry(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_check_repository(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_compliance(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_config(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_ascl_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_bintray_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_citation_file(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_citationcff_file(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_codemeta_file(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_conda_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_core_infrastructures_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_cran_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_crates_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_license(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_maven_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_npm_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_open_repository(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_pypi_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_rsd_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_zenodo_badge(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_has_zenodo_metadata_file(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_is_on_github_marketplace(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_readme(self, mocked_checker):
        pass

    @pytest.mark.skip
    def test_repo(self, mocked_checker):
        pass
