from abc import ABC, abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_filename(self, mocked_readme):
        pass

    @abstractmethod
    def test_text(self, mocked_readme):
        pass

    @abstractmethod
    def test_fmt(self, mocked_readme):
        pass

    @abstractmethod
    def test_get_compliance(self, mocked_readme):
        pass
