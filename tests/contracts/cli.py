from abc import ABC, abstractmethod


class Contract(ABC):
    @abstractmethod
    def test_version_option(self, invoke_cli):
        pass

    @abstractmethod
    def test_show_default_config(self, invoke_cli):
        pass

    @abstractmethod
    def test_with_an_url(self, invoke_cli):
        pass
