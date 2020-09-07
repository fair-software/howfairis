import sys
import requests
from colorama import Style, Fore

from howfairis.mixins import RepositoryMixin
from howfairis.mixins import LicenseMixin
from howfairis.mixins import RegistryMixin
from howfairis.mixins import CitationMixin
from howfairis.mixins import ChecklistMixin


class HowFairIsChecker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    def __init__(self, url):
        super().__init__()
        assert url.startswith("https://github.com/"), \
            "url should start with https://github.com"
        self.url = url
        self.readme = None
        self.repository_is_compliant = None
        self.license_is_compliant = None
        self.registry_is_compliant = None
        self.citation_is_compliant = None
        self.checklist_is_compliant = None
        self.badge = None
        self.owner = None
        self.repo = None
        self.readme_filename = None
        self.branch = None
        self.compliant_symbol = "\u25CF"
        self.noncompliant_symbol = "\u25CB"

    def check_badge(self):

        compliance_bool = [
            self.repository_is_compliant, self.license_is_compliant,
            self.registry_is_compliant, self.citation_is_compliant,
            self.checklist_is_compliant
        ]

        compliance_unicode = [None] * 5
        for i, c in enumerate(compliance_bool):
            if c is True:
                compliance_unicode[i] = self.compliant_symbol
            else:
                compliance_unicode[i] = self.noncompliant_symbol

        compliance_string = "%20%20".join(
            [requests.utils.quote(symbol) for symbol in compliance_unicode])

        score = compliance_bool.count(True)
        if score in [0, 1]:
            color_string = "red"
        elif score in [2, 3, 4]:
            color_string = "orange"
        elif score == 5:
            color_string = "green"

        self.badge = "[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-{0}-{1})]({2})"\
                     .format(compliance_string, color_string, "https://fair-software.eu")

        print("\nCalculated compliance: " + " ".join(compliance_unicode) + "\n")

        if self.readme is None:
            sys.exit(1)
        elif self.readme.find(self.badge) == -1:
            print("While searching through your README.md, I" +
                  " did not find the expected badge:\n" + self.badge + "\n")
            sys.exit(1)
        else:
            print("Expected badge is equal to the actual badge. " +
                  "It's all good.\n")
            sys.exit(0)

    def check_checklist(self):
        print("(5/5) checklist")
        results = [
            self.has_core_infrastructures_badge(),
            self.has_sonarcloud_badge()
        ]
        self.checklist_is_compliant = True in results
        return self

    def check_citation(self):
        print("(4/5) citation")
        results = [
            self.has_zenodo_badge(),
            self.has_citationcff_file(),
            self.has_citation_file(),
            self.has_zenodo_metadata_file(),
            self.has_codemeta_file()
        ]
        self.citation_is_compliant = True in results
        return self

    def check_license(self):
        print("(2/5) license")
        results = [self.has_license()]
        self.license_is_compliant = True in results
        return self

    def check_registry(self):
        print("(3/5) registry")
        results = [
            self.has_pypi_badge(),
            self.has_conda_badge(),
            self.has_bintray_badge(),
            self.is_on_github_marketplace()
        ]
        self.registry_is_compliant = True in results
        return self

    def check_repository(self):
        print("(1/5) repository")
        results = [self.has_open_repository()]
        self.repository_is_compliant = True in results
        return self

    def deconstruct_url(self):
        self.owner, self.repo = self.url.replace("https://github.com/",
                                                 "").split("/")[:2]
        self.branch = "master"
        self.readme_filename = "README.md"
        return self

    def get_readme(self):
        # only github urls supported
        # only README.md supported

        raw_url = "https://raw.githubusercontent.com/" + \
                  "{0}/{1}/{2}/{3}".format(self.owner, self.repo,
                                           self.branch, self.readme_filename)
        try:
            response = requests.get(raw_url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return self
        except Exception as err:
            print(f"Other error occurred: {err}")

        self.readme = response.text
        return self

    @staticmethod
    def print_state(check_name="", state=None, indent=8):
        if state is True:
            print(" " * indent + check_name + ": " + Style.BRIGHT + Fore.GREEN + str(state).lower() + Style.RESET_ALL)
        elif state is False:
            print(" " * indent + check_name + ": " + str(state).lower())
