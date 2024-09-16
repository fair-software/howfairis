from abc import ABC, abstractmethod
from requests_mock.mocker import Mocker


class Contract(ABC):

    @abstractmethod
    def test_check_checklist(self, mocked_context: Mocker, captured_output):
        pass

    @abstractmethod
    def test_check_citation(self, mocked_context: Mocker, captured_output):
        pass

    @abstractmethod
    def test_check_license(self, mocked_context: Mocker, captured_output):
        pass

    @abstractmethod
    def test_check_registry(self, mocked_context: Mocker, captured_output):
        pass

    @abstractmethod
    def test_check_repository(self, mocked_context: Mocker, captured_output):
        pass

    @abstractmethod
    def test_compliance(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_ascl_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_bintray_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_citation_file(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_citationcff_file(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_codemeta_file(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_conan_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_conda_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_core_infrastructures_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_cran_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_crates_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_license(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_maven_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_npm_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_open_repository(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_pypi_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_rsd_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_zenodo_badge(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_has_zenodo_metadata_file(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_is_on_github_marketplace(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_readme(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_repo(self, mocked_context: Mocker):
        pass
