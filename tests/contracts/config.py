from abc import ABC, abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_force_checklist(self, mocked_config):
        pass

    @abstractmethod
    def test_force_citation(self, mocked_config):
        pass

    @abstractmethod
    def test_force_license(self, mocked_config):
        pass

    @abstractmethod
    def test_force_registry(self, mocked_config):
        pass

    @abstractmethod
    def test_force_repository(self, mocked_config):
        pass

    @abstractmethod
    def test_include_comments(self, mocked_config):
        pass
