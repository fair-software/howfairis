from abc import ABC, abstractmethod
from requests_mock.mocker import Mocker


class Contract(ABC):

    @abstractmethod
    def test_api(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_branch(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_config_file(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_default_branch(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_owner(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_path(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_platform(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_raw_url_format_string(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_repo(self, mocked_context: Mocker):
        pass

    @abstractmethod
    def test_url(self, mocked_context: Mocker):
        pass

