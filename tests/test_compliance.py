from howfairis import Compliance
from howfairis.readme import Readme
from howfairis.readme_format import ReadmeFormat


def test_get_compliance():
    text = "some bogus text here but then we see the badge https://img.shields.io/badge/fair--software.eu-" + \
           "%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow with some trailing stuff."
    actual_compliance = Readme(filename="README.md", text=text, file_format=ReadmeFormat.MARKDOWN).get_compliance()
    expected_compliance = Compliance(repository=True, license_=True, registry=True, citation=True, checklist=False)
    assert actual_compliance == expected_compliance

