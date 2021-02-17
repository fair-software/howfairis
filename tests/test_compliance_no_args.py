import pytest
from howfairis import Compliance
from howfairis.readme_format import ReadmeFormat
from tests.contracts.compliance import Contract


@pytest.fixture
def compliance_fixture():
    return Compliance()


class TestComplianceNoArgs(Contract):

    def test_as_unicode(self, compliance_fixture):
        assert compliance_fixture.as_unicode() == ["\u25CB"] * 5

    def test_calc_badge_markdown(self, compliance_fixture):
        expected_badge = "[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8B%20%20%E2" \
                         "%97%8B%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B-red)](https://fair-software.eu)"
        assert compliance_fixture.calc_badge(ReadmeFormat.MARKDOWN) == expected_badge

    def test_calc_badge_restructured_text(self, compliance_fixture):
        expected_badge = ".. image:: https://img.shields.io/badge/fair--software.eu-%E2%97%8B%20%20%E2%97%8B%20" \
                         "%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B-red\n   :target: https://fair-software.eu"
        assert compliance_fixture.calc_badge(ReadmeFormat.RESTRUCTUREDTEXT) == expected_badge

    def test_checklist(self, compliance_fixture):
        assert compliance_fixture.checklist is False

    def test_citation(self, compliance_fixture):
        assert compliance_fixture.citation is False

    def test_count(self, compliance_fixture):
        assert compliance_fixture.count() == 0
        assert compliance_fixture.count(True) == 0
        assert compliance_fixture.count(False) == 5

    def test_equality_eq(self, compliance_fixture):
        expected_compliance = Compliance(False, False, False, False, False)
        assert expected_compliance == compliance_fixture

    def test_equality_ne(self, compliance_fixture):
        expected_compliances = [Compliance(True, False, False, False, False),
                                Compliance(True, True, True, True, True)]
        for expected_compliance in expected_compliances:
            assert expected_compliance != compliance_fixture

    def test_registry(self, compliance_fixture):
        assert compliance_fixture.registry is False

    def test_repo_license(self, compliance_fixture):
        assert compliance_fixture.repo_license is False

    def test_repository(self, compliance_fixture):
        assert compliance_fixture.repository is False

    def test_urlencode(self, compliance_fixture):
        expected_urlstr = "%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B"
        assert compliance_fixture.urlencode() == expected_urlstr
