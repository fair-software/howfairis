import inspect
import re
import requests
import yaml
from colorama import Fore
from colorama import Style
from howfairis.mixins import ChecklistMixin
from howfairis.mixins import CitationMixin
from howfairis.mixins import LicenseMixin
from howfairis.mixins import RegistryMixin
from howfairis.mixins import RepositoryMixin
from howfairis.Compliance import Compliance
from howfairis.ReadmeFormat import ReadmeFormat
from howfairis.Readme import Readme
from howfairis.schema import validate_against_schema


class HowFairIsChecker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    def __init__(self, repo, config_file=None, include_comments=False):
        super().__init__()
        self.compliance = None
        self.config = None
        self.config_file = ".howfairis.yml" if config_file is None else config_file
        self.readme = None
        self.include_comments = include_comments
        self.repo = repo

        self._load_config(has_user_input=config_file is not None)
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

            if self.include_comments is True:
                text = response.text
            else:
                text = remove_comments(response.text)
            self.readme = Readme(filename=readme_filename, text=text, fmt=readme_fmt)
            return self

        print("Did not find a README[.md|.rst] file at " + raw_url.replace(readme_filename, ""))
        self.readme = Readme(filename=None, text=None, fmt=None)
        return self

    def _load_config(self, has_user_input):

        raw_url = self.repo.raw_url_format_string.format(self.config_file)
        try:
            response = requests.get(raw_url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            print("Using the configuration file {0}".format(raw_url))
        except requests.HTTPError as e:
            self.config = dict()
            if has_user_input:
                raise Exception("Could not find the configuration file {0}".format(raw_url)) from e
            return self

        try:
            config = yaml.safe_load(response.text)
        except Exception as e:
            raise Exception("Problem loading YAML configuration from file {0}".format(raw_url)) from e

        try:
            validate_against_schema(config)
        except Exception as e:
            raise Exception("Configuration file should follow the schema.") from e

        self.config = config
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
