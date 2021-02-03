from abc import ABC, abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_api(self):
        pass

    @abstractmethod
    def test_branch(self):
        pass

    @abstractmethod
    def test_default_branch(self):
        pass

    @abstractmethod
    def test_url(self):
        pass
