import sys
import re
import inspect
import yaml
import requests
from colorama import Style, Fore

from howfairis.mixins import RepositoryMixin
from howfairis.mixins import LicenseMixin
from howfairis.mixins import RegistryMixin
from howfairis.mixins import CitationMixin
from howfairis.mixins import ChecklistMixin


class HowFairIsChecker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    def __init__(self, url, config_file=None, branch="master", path=""):
        super().__init__()
        assert url.startswith("https://github.com/"), "url should start with https://github.com"
        self.badge = None
        self.branch = branch
        self.checklist_is_compliant = None
        self.citation_is_compliant = None
        self.compliant_symbol = "\u25CF"
        self.config = None
        self.config_file = config_file
        self.license_is_compliant = None
        self.noncompliant_symbol = "\u25CB"
        self.owner = None
        self.path = path.strip("/")
        self.readme = None
        self.readme_filename = None
        self.registry_is_compliant = None
        self.repo = None
        self.repository_is_compliant = None
        self.url = url

        self._deconstruct_url()
        self._load_config()
        self._get_readme()

    def _eval_regexes(self, regexes, check_name=None):
        if check_name is None:
            # get name of the function who's calling me
            check_name = inspect.stack()[1].function
        if self.readme is None:
            self._print_state(check_name=check_name, state=False)
            return False
        for regex in regexes:
            if re.compile(regex).search(self.readme) is not None:
                self._print_state(check_name=check_name, state=True)
                return True
        self._print_state(check_name=check_name, state=False)
        return False

    def _deconstruct_url(self):
        self.owner, self.repo = self.url.replace("https://github.com/", "").split("/")[:2]
        return self

    def _get_readme(self):
        for readme_filename in ["README.rst", "README.md"]:
            raw_url = "https://raw.githubusercontent.com/{0}/{1}/{2}/{3}/{4}"\
                      .format(self.owner, self.repo, self.branch, self.path, readme_filename)
            try:
                response = requests.get(raw_url)
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                continue

            self.readme_filename = readme_filename
            self.readme = response.text
            return self

        print("Did not find a README[.md|.rst] file.")
        return self

    def _load_config(self):

        s = ".howfairis.yml" if self.config_file is None else self.config_file
        raw_url = "https://raw.githubusercontent.com/{0}/{1}/{2}/{3}/{4}" \
            .format(self.owner, self.repo, self.branch, self.path, s)
        try:
            response = requests.get(raw_url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            print("Using the configuration file from {0}".format(raw_url))
        except requests.HTTPError:
            self.config = dict()
            if self.config_file is not None:
                print("Could not find the configuration file at {0}".format(raw_url))
            return self

        config = yaml.safe_load(response.text)
        if config is None:
            config = dict()
        if not isinstance(config, dict):
            raise ValueError("Unexpected configuration file contents.")
        self.config = config
        return self

    @staticmethod
    def _print_state(check_name="", state=None, indent=6):
        if state is True:
            print(" " * indent + Style.BRIGHT + Fore.GREEN + "\u2713 " + Style.RESET_ALL + check_name)
        elif state is False:
            print(" " * indent + Style.BRIGHT + Fore.RED + "\u00D7 " + Style.RESET_ALL + check_name)

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
        elif score in [2, 3]:
            color_string = "orange"
        elif score in [4]:
            color_string = "yellow"
        elif score == 5:
            color_string = "green"

        badge_url = "https://img.shields.io/badge/fair--software.eu-{0}-{1}".format(compliance_string, color_string)
        if self.readme_filename in ["README.rst", "readme.rst"]:
            self.badge = ".. image:: {0}\n   :target: {1}".format(badge_url, "https://fair-software.eu")
        elif self.readme_filename in ["README.md", "readme.md"]:
            self.badge = "[![fair-software.eu]({0})]({1})".format(badge_url, "https://fair-software.eu")

        print("\nCalculated compliance: " + " ".join(compliance_unicode) + "\n")

        if self.readme is None:
            sys.exit(1)
        elif self.readme.find(badge_url) == -1:
            print("While searching through your {0}, I did not find the expected badge:\n{1}"
                  .format(self.readme_filename, self.badge))
            sys.exit(1)
        else:
            print("Expected badge is equal to the actual badge. It's all good.\n")
            sys.exit(0)

    def check_five_recommendations(self):
        self.repository_is_compliant = self.check_repository()
        self.license_is_compliant = self.check_license()
        self.registry_is_compliant = self.check_registry()
        self.citation_is_compliant = self.check_citation()
        self.checklist_is_compliant = self.check_checklist()
