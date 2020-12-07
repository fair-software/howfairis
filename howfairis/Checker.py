import inspect
import re
import requests
from colorama import Fore
from colorama import Style
from howfairis.Compliance import Compliance
from howfairis.mixins import ChecklistMixin
from howfairis.mixins import CitationMixin
from howfairis.mixins import LicenseMixin
from howfairis.mixins import RegistryMixin
from howfairis.mixins import RepositoryMixin
from howfairis.Readme import Readme
from howfairis.ReadmeFormat import ReadmeFormat


class Checker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    def __init__(self, config, repo):
        super().__init__()
        self.compliance = None
        self.config = config
        self.readme = None
        self.repo = repo

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
        def remove_comments(text):
            return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

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

            if self.config.merged.get("include_comments") is True:
                text = response.text
            else:
                text = remove_comments(response.text)
            self.readme = Readme(filename=readme_filename, text=text, fmt=readme_fmt)
            return self

        print("Did not find a README[.md|.rst] file at " + raw_url.replace(readme_filename, ""))
        self.readme = Readme(filename=None, text=None, fmt=None)
        return self

    @staticmethod
    def _print_state(check_name="", state=None, indent=6):
        if state is True:
            print(" " * indent + Style.BRIGHT + Fore.GREEN + "\u2713 " + Style.RESET_ALL + check_name)
        elif state is False:
            print(" " * indent + Style.BRIGHT + Fore.RED + "\u00D7 " + Style.RESET_ALL + check_name)

    def check_five_recommendations(self):
        self.compliance = Compliance(repository=self.check_repository(),
                                     license_=self.check_license(),
                                     registry=self.check_registry(),
                                     citation=self.check_citation(),
                                     checklist=self.check_checklist())
        return self
