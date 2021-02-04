from abc import ABC, abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_default(self, mocked_config):
        pass

    @abstractmethod
    def test_repo(self, mocked_config):
        pass

    @abstractmethod
    def test_user(self, mocked_config):
        pass
