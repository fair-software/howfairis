from abc import ABC
from abc import abstractmethod
from requests_mock.mocker import Mocker


class Contract(ABC):

    @abstractmethod
    def test_api(self, mocker: Mocker):
        pass

    @abstractmethod
    def test_branch(self, mocker: Mocker):
        pass

    @abstractmethod
    def test_default_branch(self, mocker: Mocker):
        pass

    @abstractmethod
    def test_owner(self, mocker: Mocker):
        pass

    @abstractmethod
    def test_path(self, mocker: Mocker):
        pass

    @abstractmethod
    def test_platform(self, mocker: Mocker):
        pass

    @abstractmethod
    def test_raw_url_format_string(self, mocker: Mocker):
        pass

    @abstractmethod
    def test_repo(self, mocker: Mocker):
        pass

    @abstractmethod
    def test_url(self, mocker: Mocker):
        pass
