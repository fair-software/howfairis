from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_show_default_config(self, invoke_cli):
        pass

    @abstractmethod
    def test_version_option(self, invoke_cli):
        pass

    @abstractmethod
    def test_with_a_url(self, invoke_cli):
        pass

    @abstractmethod
    def test_with_nonexistent_path(self, invoke_cli):
        # Should raise warning about path not there
        # Incorrect path means that we dont have a README, in turn that means exit code should be nonzero
        pass
