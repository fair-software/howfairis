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
from howfairis.Platform import Platform
from howfairis.ReadmeFormat import ReadmeFormat
from howfairis.schema import validate_against_schema


class HowFairIsChecker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    # pylint: disable=too-many-arguments
    def __init__(self, url, config_file=None, branch=None, path=None, include_comments=False):
        super().__init__()
        self.branch = "master" if branch is None else branch
        self.checklist_is_compliant = None
        self.citation_is_compliant = None
        self.config = None
        self.config_file = ".howfairis.yml" if config_file is None else config_file
        self.license_is_compliant = None
        self.owner = None
        self.path = "" if path is None else "/" + path.strip("/")
        self.platform = None
        self.raw_url_format_string = None
        self.readme = None
        self.registry_is_compliant = None
        self.include_comments = include_comments
        self.repo = None
        self.repository_is_compliant = None
        self.url = url

        self._deconstruct_url()
        self._load_config(has_user_input=config_file is not None)
        self._get_readme()

    def _eval_regexes(self, regexes, check_name=None):
        if check_name is None:
            # get name of the function who's calling me
            check_name = inspect.stack()[1].function
        if self.readme["text"] is None:
            self._print_state(check_name=check_name, state=False)
            return False
        for regex in regexes:
            if re.compile(regex).search(self.readme["text"]) is not None:
                self._print_state(check_name=check_name, state=True)
                return True
        self._print_state(check_name=check_name, state=False)
        return False

    def _deconstruct_url(self):
        assert self.url.startswith("https://"), "url should start with https://"
        assert True in [self.url.startswith("https://github.com"),
                        self.url.startswith("https://gitlab.com")], "Repository should be on GitHub or on GitLab."

        if self.url.startswith("https://github.com"):
            self.platform = Platform.GITHUB
            self.raw_url_format_string = "https://raw.githubusercontent.com/{0}/{1}/{2}{3}/{4}"
            try:
                self.owner, self.repo = self.url.replace("https://github.com", "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e
        elif self.url.startswith("https://gitlab.com"):
            self.platform = Platform.GITLAB
            self.raw_url_format_string = "https://gitlab.com/{0}/{1}/-/raw/{2}{3}/{4}"
            try:
                self.owner, self.repo = self.url.replace("https://gitlab.com", "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e

        if self.owner == "" or self.repo == "":
            raise ValueError("Bad value for input argument URL.")

        return self

    def _get_readme(self):
        def remove_comments(text):
            return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

        for readme_filename in ["README.rst", "README.md"]:
            raw_url = self.raw_url_format_string.format(self.owner, self.repo, self.branch, self.path, readme_filename)
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
            self.readme = dict(filename=readme_filename, text=text, fmt=readme_fmt)
            return self

        print("Did not find a README[.md|.rst] file at " + raw_url.replace(readme_filename, ""))
        self.readme = dict(filename=None, text=None, fmt=None)
        return self

    def _load_config(self, has_user_input):

        raw_url = self.raw_url_format_string.format(self.owner, self.repo, self.branch, self.path, self.config_file)
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
        self.repository_is_compliant = self.check_repository()
        self.license_is_compliant = self.check_license()
        self.registry_is_compliant = self.check_registry()
        self.citation_is_compliant = self.check_citation()
        self.checklist_is_compliant = self.check_checklist()
        return self

    @property
    def compliance(self):
        return [self.repository_is_compliant,
                self.license_is_compliant,
                self.registry_is_compliant,
                self.citation_is_compliant,
                self.checklist_is_compliant]
