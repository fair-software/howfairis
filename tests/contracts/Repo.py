from abc import ABC, abstractmethod
from requests_mock import Mocker


class Contract(ABC):

    @abstractmethod
    def test_url(self, mocker: Mocker):
        pass
