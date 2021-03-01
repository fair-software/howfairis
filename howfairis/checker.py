import inspect
import os
import re
from typing import Optional
import requests
from colorama import Fore
from colorama import Style
from ruamel.yaml import YAML
from voluptuous.error import Invalid
from voluptuous.error import MultipleInvalid
from .compliance import Compliance
from .get_apikeys_from_env_vars import get_apikeys_from_env_vars
from .mixins.checklist_mixin import ChecklistMixin
from .mixins.citation_mixin import CitationMixin
from .mixins.license_mixin import LicenseMixin
from .mixins.registry_mixin import RegistryMixin
from .mixins.repository_mixin import RepositoryMixin
from .readme import Readme
from .readme_format import ReadmeFormat
from .repo import Repo
from .requesting.get_from_platform import get_from_platform
from .schema import validate_against_schema


DEFAULT_CONFIG_FILENAME = ".howfairis.yml"


class Checker(RepositoryMixin, LicenseMixin, RegistryMixin, CitationMixin, ChecklistMixin):
    """Check the repo against the five FAIR software recommendations using supplied config.

    Args:
        repo: Repository to check
        user_config_filename: Filename of configuration file on users local filesystem.
        repo_config_filename: Filename of configuration file on the repository.
            Default is ".howfairis.yml".
        ignore_repo_config: If True then the configuration file on the repository is not loaded.
            Default is False.
        is_quiet: If True then less verbose output is printed. Default is False.

    Example:

        The registry compliance of the ``https://github.com/fair-software/howfairis`` repository can be checked with:

        .. code-block ::

           >>> from howfairis import Repo, Checker
           >>> url = "https://github.com/fair-software/howfairis"
           >>> repo = Repo(url)
           >>> checker = Checker(repo, is_quiet=True)
           ...
           >>> compliance = checker.check_five_recommendations()
           >>> compliance.registry
           True

    Attributes:
        repo (.repo.Repo): Object describing the properties of the target repository.
        is_quiet (bool): If True then less verbose output is printed. Default is False.
        readme (.readme.Readme): Retrieved README from the repository.

    The ``skip_*_checks_reason`` and :attr:`Checker.ignore_commented_badges` properties are set based on merger of

    1. the default configuration (see :download:`howfairis/data/.howfairis.yml </../howfairis/data/.howfairis.yml>`),
    2. config file from repo and
    3. config file from users local filesystem.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, repo: Repo,
                 user_config_filename: Optional[str] = None,
                 repo_config_filename: str = DEFAULT_CONFIG_FILENAME,
                 ignore_repo_config: bool = False, is_quiet: bool = False):

        super().__init__()
        self.repo = repo
        self.is_quiet = is_quiet
        self._apikeys = get_apikeys_from_env_vars()
        self._default_config = Checker._load_default_config()
        self._repo_config = self._load_repo_config(repo_config_filename, ignore_repo_config)
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
        for readme_filename in ["README.rst", "README.md"]:
            raw_url = self.repo.raw_url_format_string.format(readme_filename)
            try:
                response = get_from_platform(self.repo.platform, raw_url, "raw", apikeys=self._apikeys)
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                continue

            if readme_filename == "README.rst":
                readme_file_format = ReadmeFormat.RESTRUCTUREDTEXT
            elif readme_filename == "README.md":
                readme_file_format = ReadmeFormat.MARKDOWN
            else:
                readme_file_format = None

            return Readme(filename=readme_filename, text=response.text, file_format=readme_file_format,
                          ignore_commented_badges=self.ignore_commented_badges)

        print("\nDid not find a README[.md|.rst] file at {0}\nProceeding without it -- expect the"
              " compliance to suffer.\n".format(raw_url.replace(readme_filename, "")))

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

    def _load_repo_config(self, repo_config_filename, ignore_remote_config):
        if self.repo is None:
            return dict()

        if ignore_remote_config is True:
            return dict()

        raw_url = self.repo.raw_url_format_string.format(repo_config_filename)
        non_default_repo_config_filename = repo_config_filename != DEFAULT_CONFIG_FILENAME

        try:
            response = get_from_platform(self.repo.platform, raw_url, "raw", apikeys=self._apikeys)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            if non_default_repo_config_filename:
                print("Using the configuration file {0}".format(raw_url))
        except requests.HTTPError as e:
            if non_default_repo_config_filename:
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

        if os.path.isabs(user_config_filename):
            p = user_config_filename
        else:
            p = os.path.join(os.getcwd(), user_config_filename)

        if not os.path.exists(p):
            raise FileNotFoundError("{0} doesn't exist.".format(user_config_filename))

        with open(user_config_filename, "rt") as f:
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

    def _print_state(self, check_name="", state=None, indent=6):
        if not self.is_quiet:
            if state is True:
                print(" " * indent + Style.BRIGHT + Fore.GREEN + "\u2713 " + Style.RESET_ALL + check_name)
            elif state is False:
                print(" " * indent + Style.BRIGHT + Fore.RED + "\u00D7 " + Style.RESET_ALL + check_name)

    def check_five_recommendations(self) -> Compliance:
        """Check the repo against the five FAIR software recommendations

        Returns: compliance result
        """
        return Compliance(repository=self.check_repository(),
                          license_=self.check_license(),
                          registry=self.check_registry(),
                          citation=self.check_citation(),
                          checklist=self.check_checklist())

    @property
    def skip_repository_checks_reason(self) -> bool:
        """bool: If True then checks for the repository recommendation are skipped
        and the recommendation is marked as compliant"""
        return self._merged_config.get("skip_repository_checks_reason", None)

    @property
    def skip_license_checks_reason(self) -> bool:
        """bool: If True then checks for the license recommendation are skipped
        and the recommendation is marked as compliant"""
        return self._merged_config.get("skip_license_checks_reason", None)

    @property
    def skip_registry_checks_reason(self) -> bool:
        """bool: If True then checks for the registry recommendation are skipped
        and the recommendation is marked as compliant"""
        return self._merged_config.get("skip_registry_checks_reason", None)

    @property
    def skip_citation_checks_reason(self) -> bool:
        """bool: If True then checks for the citation recommendation are skipped
        and the recommendation is marked as compliant"""
        return self._merged_config.get("skip_citation_checks_reason", None)

    @property
    def skip_checklist_checks_reason(self) -> bool:
        """bool: If True then checks for the checklist recommendation are skipped
        and the recommendation is marked as compliant"""
        return self._merged_config.get("skip_checklist_checks_reason", None)

    @property
    def ignore_commented_badges(self) -> bool:
        """bool: If True then any commented out badges in the README of the repository are ignored."""
        return self._merged_config.get("ignore_commented_badges")
