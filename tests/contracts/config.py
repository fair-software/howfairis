from abc import ABC, abstractmethod
from requests_mock.mocker import Mocker


class Contract(ABC):

    @abstractmethod
    def test_force_checklist(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_force_citation(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_force_license(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_force_registry(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_force_repository(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_include_comments(self, mocked_context: Mocker):
        pass
