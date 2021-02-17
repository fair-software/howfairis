from abc import ABC, abstractmethod
from howfairis import Compliance


class Contract(ABC):

    @abstractmethod
    def test_as_unicode(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_calc_badge_markdown(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_calc_badge_restructured_text(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_checklist(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_citation(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_count(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_equality_eq(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_equality_ne(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_registry(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_repo_license(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_repository(self, compliance_fixture: Compliance):
        pass

    @abstractmethod
    def test_urlencode(self, compliance_fixture: Compliance):
        pass
