import re
from typing import Optional
import requests
from .code_repository_platforms import Platform
from .exceptions.get_default_branch_exception import GetDefaultBranchException
from .get_apikeys_from_env_vars import get_apikeys_from_env_vars
from .requesting.get_from_platform import get_from_platform


class Repo:
    """Representation of a source code repository.

    Args:
        url: URL of a code repository such as https://github.com/fair-software/howfairis
        branch: Branch to checkout. Defaults to default branch of the repository.
            Can also be a commit SHA-1 hash or tag.
        path: Path inside repository. Defaults to root.

    Attributes:
        url (str): URL of a code repository,
        branch (str, None): Branch to checkout. If None then :attr:`Repo.default_branch` will be used.
        path (str): Path inside repository.
        platform (.code_repository_platforms.Platform): Detected code repository platform of repo.
        owner (str): Owner of the repo.
        repo (str): Name of repo. Normally the last part of the url.
        api (str): API endpoint of code repository platform where info about repo can be fetched.
        default_branch (str, None): The default branch of the repo on the code repository platform.
        raw_url_format_string (str): URL where a file from repo can be downloaded.
            URL has single placeholder for filename.

    """
    def __init__(self, url: str, branch: Optional[str] = None, path: Optional[str] = None):
        # run assertions on user input
        Repo._check_assertions(url)

        # assign arguments to instance members
        self.url = url
        self.branch = branch
        self.path = "" if path is None else "/" + path.strip("/")

        # assign remaining members as needed
        self._apikeys = get_apikeys_from_env_vars()
        self.platform = self._derive_platform()
        self.owner, self.repo = self._derive_owner_and_repo()
        self.api = self._derive_api()
        self.default_branch = self._get_default_branch()
        self.raw_url_format_string = self._derive_raw_url_format_string()

    @staticmethod
    def _check_assertions(url):
        assert url.startswith("https://"), "url should start with https://"
        assert True in [url.startswith("https://github.com"),
                        url.startswith("https://gitlab.com")], "Repository should be on github.com or on gitlab.com."
        assert re.search("^https://git(hub|lab).com/[^/]+/[^/]+", url), "url is not a repository"

    def _derive_api(self):
        if self.platform == Platform.GITHUB:
            api = "https://api.github.com/repos/{0}/{1}".format(self.owner, self.repo)
        elif self.platform == Platform.GITLAB:
            api = "https://gitlab.com/api/v4/projects/{0}%2F{1}".format(self.owner, self.repo)
        return api

    def _derive_owner_and_repo(self):
        if self.platform == Platform.GITHUB:
            try:
                owner, repo = self.url.replace("https://github.com", "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e

        elif self.platform == Platform.GITLAB:
            try:
                owner, repo = self.url.replace("https://gitlab.com", "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e

        if owner == "" or repo == "":
            raise ValueError("Bad value for input argument URL.")

        return owner, repo

    def _derive_platform(self):
        if self.url.startswith("https://github.com"):
            return Platform.GITHUB

        if self.url.startswith("https://gitlab.com"):
            return Platform.GITLAB

        return None

    def _derive_raw_url_format_string(self):
        if self.branch is not None:
            # User specified a branch, use that regardless of whether it actually exists
            branch = self.branch
        else:
            branch = self.default_branch

        if self.platform == Platform.GITHUB:
            raw_url_format_string = "https://raw.githubusercontent.com/{0}/{1}/{2}{3}" \
                                    .format(self.owner, self.repo, branch, self.path) + "/{0}"

        elif self.platform == Platform.GITLAB:
            raw_url_format_string = "https://gitlab.com/{0}/{1}/-/raw/{2}{3}" \
                                    .format(self.owner, self.repo, branch, self.path) + "/{0}"

        return raw_url_format_string

    def _get_default_branch(self):

        if self.branch is not None:
            # user has specified a branch, use that regardless of whether it actually exists
            return None

        # GitHub API and GitLab API work the same
        response = get_from_platform(self.platform, self.api, "api", apikeys=self._apikeys)
        # If the request was successful, the next line will not raise any Exception
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise GetDefaultBranchException("Something went wrong asking the repo for its default branch.") from e
        return response.json().get("default_branch")
