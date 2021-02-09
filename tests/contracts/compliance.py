from abc import ABC, abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_as_unicode(self, compliance_fixture):
        pass

    @abstractmethod
    def test_calc_badge_markdown(self, compliance_fixture):
        pass

    @abstractmethod
    def test_calc_badge_restructured_text(self, compliance_fixture):
        pass

    @abstractmethod
    def test_checklist(self, compliance_fixture):
        pass

    @abstractmethod
    def test_citation(self, compliance_fixture):
        pass

    @abstractmethod
    def test_compliant_symbol(self, compliance_fixture):
        pass

    @abstractmethod
    def test_count(self, compliance_fixture):
        pass

    @abstractmethod
    def test_equality_eq(self, compliance_fixture):
        pass

    @abstractmethod
    def test_equality_ge(self, compliance_fixture):
        pass

    @abstractmethod
    def test_equality_gt(self, compliance_fixture):
        pass

    @abstractmethod
    def test_equality_le(self, compliance_fixture):
        pass

    @abstractmethod
    def test_equality_lt(self, compliance_fixture):
        pass

    @abstractmethod
    def test_equality_ne(self, compliance_fixture):
        pass

    @abstractmethod
    def test_license(self, compliance_fixture):
        pass

    @abstractmethod
    def test_noncompliant_symbol(self, compliance_fixture):
        pass

    @abstractmethod
    def test_registry(self, compliance_fixture):
        pass

    @abstractmethod
    def test_repository(self, compliance_fixture):
        pass

    @abstractmethod
    def test_urlencode(self, compliance_fixture):
        pass
