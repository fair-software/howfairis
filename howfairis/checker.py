import inspect
import re
import requests
from colorama import Fore
from colorama import Style
from howfairis.compliance import Compliance
from howfairis.config import Config
from howfairis.mixins import ChecklistMixin
from howfairis.mixins import CitationMixin
from howfairis.mixins import LicenseMixin
from howfairis.mixins import RegistryMixin
from howfairis.mixins import RepositoryMixin
from howfairis.readme import Readme
from howfairis.readme_format import ReadmeFormat
from howfairis.repo import Repo


class Checker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    """Check the repo against the five FAIR software recommendations using supplied config.

    Args:
        config: Configuration to use
        repo: Repository to check

    Attributes:
        readme (Readme): Retrieved README from the repository.
        compliance (Optional[Compliance]): The current compliance.
            Filled after :py:func:`Checker.check_five_recommendations` is called.
        badge_url (Optional[str]): URL of badge image for the current compliance.
            Filled after :py:func:`Checker.check_five_recommendations` is called.
        badge (Optional[str]): Badge image link for the current compliance. Formatted in format of README.
            Filled after :py:func:`Checker.check_five_recommendations` is called.

    """

    def __init__(self, config: Config, repo: Repo):
        super().__init__()
        self.compliance = None
        self.config = config
        self.readme = None
        self.repo = repo
        self.badge = None
        self.badge_url = None

        self._get_readme()

    def _eval_regexes(self, regexes, check_name=None):
        if check_name is None:
            # get name of the function who's calling me
            check_name = inspect.stack()[1].function
        if self.readme.text is None:
            self._print_state(check_name=check_name, state=False)
            return False
        for regex in regexes:
            if re.compile(regex).search(self.readme.text) is not None:
                self._print_state(check_name=check_name, state=True)
                return True
        self._print_state(check_name=check_name, state=False)
        return False

    def _get_readme(self):
        for readme_filename in ["README.rst", "README.md"]:
            raw_url = self.repo.raw_url_format_string.format(readme_filename)
            try:
                response = requests.get(raw_url)
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                continue

            if readme_filename == "README.md":
                readme_fmt = ReadmeFormat.MARKDOWN
            elif readme_filename == "README.rst":
                readme_fmt = ReadmeFormat.RESTRUCTUREDTEXT
            else:
                readme_fmt = None

            self.readme = Readme(filename=readme_filename,
                                 text=response.text, fmt=readme_fmt)
            if self.config.merged.get("include_comments") is False:
                self.readme.remove_comments()
            return self

        print("Did not find a README[.md|.rst] file at " +
              raw_url.replace(readme_filename, ""))
        self.readme = Readme(filename=None, text=None, fmt=None)
        return self

    @staticmethod
    def _print_state(check_name="", state=None, indent=6):
        if state is True:
            print(" " * indent + Style.BRIGHT + Fore.GREEN +
                  "\u2713 " + Style.RESET_ALL + check_name)
        elif state is False:
            print(" " * indent + Style.BRIGHT + Fore.RED +
                  "\u00D7 " + Style.RESET_ALL + check_name)

    def _calc_badge(self):
        score = self.compliance.count(True)

        if score in [0, 1]:
            color_string = "red"
        elif score in [2, 3]:
            color_string = "orange"
        elif score in [4]:
            color_string = "yellow"
        elif score == 5:
            color_string = "green"

        self.badge_url = "https://img.shields.io/badge/fair--software.eu-{0}-{1}".format(self.compliance.urlencode(),
                                                                                         color_string)
        if self.readme.fmt == ReadmeFormat.RESTRUCTUREDTEXT:
            self.badge = ".. image:: {0}\n   :target: {1}".format(
                self.badge_url, "https://fair-software.eu")
        if self.readme.fmt == ReadmeFormat.MARKDOWN:
            self.badge = "[![fair-software.eu]({0})]({1})".format(
                self.badge_url, "https://fair-software.eu")

        return self

    def check_five_recommendations(self):
        """Check the repo against the five FAIR software recommendations

        After being called the :py:attr:`.Checker.compliance` property will be filled the the result of the check.
        """
        self.compliance = Compliance(repository=self.check_repository(),
                                     license_=self.check_license(),
                                     registry=self.check_registry(),
                                     citation=self.check_citation(),
                                     checklist=self.check_checklist())
        self._calc_badge()
        return self
