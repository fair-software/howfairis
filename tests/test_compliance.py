import pytest
from howfairis import Compliance
from howfairis.readme import Readme
from howfairis.readme_format import ReadmeFormat


def test_get_compliance():
    text = "some bogus text here but then we see the badge https://img.shields.io/badge/fair--software.eu-" + \
           "%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow with some trailing stuff."
    actual_compliance = Readme(filename="README.md", text=text, file_format=ReadmeFormat.MARKDOWN).get_compliance()
    expected_compliance = Compliance(repository=True, license_=True, registry=True, citation=True, checklist=False)
    assert actual_compliance == expected_compliance


def test_get_compliance_json():
    expected_compliance = {'checklist': False, 'citation': True, 'license': True, 'registry': True, 'repository': True}
    actual_compliance = Compliance(repository=True, license_=True, registry=True, citation=True, checklist=False).as_json()
    assert actual_compliance == expected_compliance

    expected_compliance = {'checklist': True, 'citation': True, 'license': True, 'registry': False, 'repository': True}
    actual_compliance = Compliance(repository=True, license_=True, registry=False, citation=True, checklist=True).as_json()
    assert actual_compliance == expected_compliance


@pytest.mark.parametrize("compliance,expected", [
    (Compliance(True, True, True, True, True), "green"),
    (Compliance(True, True, True, True, False), "yellow"),
    (Compliance(True, True, True, False, False), "orange"),
    (Compliance(True, True, False, False, False), "orange"),
    (Compliance(True, False, False, False, False), "red"),
    (Compliance(False, False, False, False, False), "red"),
])
def test_color(compliance, expected):
    assert compliance.color() == expected
