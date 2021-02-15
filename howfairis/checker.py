import inspect
import os
import re
from datetime import datetime
from datetime import timedelta
import requests
from colorama import Fore
from colorama import Style
from dateutil import tz
from ruamel.yaml import YAML
from voluptuous.error import Invalid
from voluptuous.error import MultipleInvalid
from howfairis.compliance import Compliance
from howfairis.mixins import ChecklistMixin
from howfairis.mixins import CitationMixin
from howfairis.mixins import LicenseMixin
from howfairis.mixins import RegistryMixin
from howfairis.mixins import RepositoryMixin
from howfairis.readme import Readme
from howfairis.readme_format import ReadmeFormat
from howfairis.repo import Repo
from howfairis.schema import validate_against_schema


class Checker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    """Check the repo against the five FAIR software recommendations using supplied config.

    Args:
        repo: Repository to check

    Attributes:
        readme (Readme): Retrieved README from the repository.
        compliance (Optional[howfairis.compliance.Compliance]): The current compliance.
            Filled after :py:func:`Checker.check_five_recommendations` is called.

    """

    def __init__(self, repo: Repo, user_config_filename=None, repo_config_filename=None, ignore_repo_config=False):
        super().__init__()
        self.compliance = None
        self.repo = repo
        self._default_config = Checker._load_default_config()
        self._repo_config = Checker._load_repo_config(repo, repo_config_filename, ignore_repo_config)
        self._user_config = Checker._load_user_config(user_config_filename)
        self._merged_config = self._merge_configurations()
        self.readme = self._get_readme()

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
                readme_file_format = ReadmeFormat.MARKDOWN
            elif readme_filename == "README.rst":
                readme_file_format = ReadmeFormat.RESTRUCTUREDTEXT
            else:
                readme_file_format = None

            if self.include_comments is True:
                text = response.text
            else:
                text = remove_comments(response.text)

            return Readme(filename=readme_filename, text=text, file_format=readme_file_format)

        print("Did not find a README[.md|.rst] file at " + raw_url.replace(readme_filename, ""))

        return Readme(filename=None, text=None, file_format=None)

    @staticmethod
    def _load_default_config():
        pkg_root = os.path.dirname(__file__)
        default_config_filename = os.path.join(pkg_root, "data", ".howfairis.yml")
        with open(default_config_filename, "rt") as f:
            text = f.read()
        default_config = YAML(typ="safe").load(text)
        if default_config is None:
            default_config = dict()
        try:
            validate_against_schema(default_config)
        except (Invalid, MultipleInvalid):
            print("Default configuration file should follow the schema for it to be considered.")
            return dict()
        return default_config

    @staticmethod
    def _load_repo_config(repo, repo_config_filename, ignore_remote_config):
        if repo is None:
            return dict()

        if ignore_remote_config is True:
            return dict()

        if repo_config_filename is None:
            raw_url = repo.raw_url_format_string.format(".howfairis.yml")
        else:
            raw_url = repo.raw_url_format_string.format(repo_config_filename)

        try:
            response = requests.get(raw_url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            print("Using the configuration file {0}".format(raw_url))
        except requests.HTTPError as e:
            if repo_config_filename is not None:
                raise Exception("Could not find the configuration file {0}".format(raw_url)) from e
            return dict()

        try:
            repo_config = YAML(typ="safe").load(response.text)
        except Exception as e:
            raise Exception("Problem loading YAML configuration from file {0}".format(raw_url)) from e

        try:
            validate_against_schema(repo_config)
        except (Invalid, MultipleInvalid):
            print("Repository's configuration file should follow the schema for it to be considered.")
            return dict()

        return repo_config

    @staticmethod
    def _load_user_config(user_config_filename):
        if user_config_filename is None:
            return dict()

        p = os.path.join(os.getcwd(), user_config_filename)
        if not os.path.exists(p):
            raise FileNotFoundError("{0} doesn't exist.".format(user_config_filename))

        with open(p, "rt") as f:
            text = f.read()
        user_config = YAML(typ="safe").load(text)
        if user_config is None:
            user_config = dict()
        try:
            validate_against_schema(user_config)
        except Exception as e:
            raise Exception("User configuration file should follow the schema.") from e
        return user_config

    def _merge_configurations(self):
        """Configuration dictionary based on merger of

            * default config from this package
            * config from repository
            * config from local user
        """
        m = dict()
        m.update(self._default_config)
        m.update(self._repo_config)
        m.update(self._user_config)
        return m

    @staticmethod
    def _print_state(check_name="", state=None, indent=6):
        if state is True:
            print(" " * indent + Style.BRIGHT + Fore.GREEN + "\u2713 " + Style.RESET_ALL + check_name)
        elif state is False:
            print(" " * indent + Style.BRIGHT + Fore.RED + "\u00D7 " + Style.RESET_ALL + check_name)

    def check_five_recommendations(self):
        """Check the repo against the five FAIR software recommendations

        After being called the :py:attr:`.Checker.compliance` property will be filled the the result of the check.
        """
        return Compliance(repository=self.check_repository(),
                          license_=self.check_license(),
                          registry=self.check_registry(),
                          citation=self.check_citation(),
                          checklist=self.check_checklist())

    def github_readme_creation_check(self):
        try:
            response = requests.get(self.repo.api)
            date_created_string = response.json().get("created_at")
            date_created_utc = datetime.strptime(date_created_string, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=tz.tzutc())
            date_created_local = date_created_utc.astimezone(tz.tzlocal())
            date_now_local = datetime.now().astimezone(tz.tzlocal())
            time_delta = date_now_local - date_created_local
            if time_delta < timedelta(minutes=5):
                print(f"Warning: Your {self.readme.filename} was updated " +
                      "less than 5 minutes ago. The effects of this update " +
                      "are not visible yet in the calculated compliance.")
            return
        except TypeError:
            return

    @property
    def skip_repository_checks_reason(self):
        return self._merged_config.get("skip_repository_checks_reason", None)

    @property
    def skip_license_checks_reason(self):
        return self._merged_config.get("skip_license_checks_reason", None)

    @property
    def skip_registry_checks_reason(self):
        return self._merged_config.get("skip_registry_checks_reason", None)

    @property
    def skip_citation_checks_reason(self):
        return self._merged_config.get("skip_citation_checks_reason", None)

    @property
    def skip_checklist_checks_reason(self):
        return self._merged_config.get("skip_checklist_checks_reason", None)

    @property
    def include_comments(self):
        return self._merged_config.get("include_comments")
