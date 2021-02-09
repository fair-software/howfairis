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

    def test_compliant_symbol(self, compliance_fixture):
        assert compliance_fixture.compliant_symbol == "\u25CF"

    def test_count(self, compliance_fixture):
        assert compliance_fixture.count() == 0

    def test_license(self, compliance_fixture):
        assert compliance_fixture.license is False

    def test_noncompliant_symbol(self, compliance_fixture):
        assert compliance_fixture.noncompliant_symbol == "\u25CB"

    def test_registry(self, compliance_fixture):
        assert compliance_fixture.registry is False

    def test_repository(self, compliance_fixture):
        assert compliance_fixture.repository is False

    def test_urlencode(self, compliance_fixture):
        expected_urlstr = "%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B"
        assert compliance_fixture.urlencode() == expected_urlstr
