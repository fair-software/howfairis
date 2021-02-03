from abc import ABC, abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_api(self):
        pass

    @abstractmethod
    def test_branch(self):
        pass

    @abstractmethod
    def test_config_file(self):
        pass

    @abstractmethod
    def test_default_branch(self):
        pass

    @abstractmethod
    def test_owner(self):
        pass

    @abstractmethod
    def test_path(self):
        pass

    @abstractmethod
    def test_platform(self):
        pass

    @abstractmethod
    def test_raw_url_format_string(self):
        pass

    @abstractmethod
    def test_repo(self):
        pass

    @abstractmethod
    def test_url(self):
        pass

