import re
import requests
from howfairis.code_repository_platforms import Platform


class Repo:
    """Publicly accessible repository with version control

    Args:
        url: URL of repository. For example https://github.com/fair-software/howfairis
        branch: Branch to checkout. Defaults to default branch of the repository platform.
            Can also be a commit SHA-1 hash or tag.
        path: Path inside repository. Defaults to root.
        config_file: Name of the configuration file to control the behavior of the howfairis package.

    """

    HTTPS_BITBUCKET_ORG = "https://bitbucket.org"
    HTTPS_GITHUB_COM = "https://github.com"
    HTTPS_GITLAB_COM = "https://gitlab.com"
    HTTPS_FOSS_HEPTAPOD_NET = "https://foss.heptapod.net"

    def __init__(self, url: str, branch=None, path=None):
        # run assertions on user input
        Repo._check_assertions(url)

        # assign arguments to instance members
        self.url = url
        self.branch = branch
        self.path = "" if path is None else "/" + path.strip("/")

        # assign remaining members as needed
        self.platform = self._derive_platform()
        self.owner, self.repo = self._derive_owner_and_repo()
        self.api = self._derive_api()
        self.default_branch = self._get_default_branch()
        self.raw_url_format_string = self._derive_raw_url_format_string()

    @staticmethod
    def _check_assertions(url):
        assert url.startswith("https://"), "url should start with https://"
        assert True in [url.startswith(Repo.HTTPS_BITBUCKET_ORG),
                        url.startswith(Repo.HTTPS_FOSS_HEPTAPOD_NET),
                        url.startswith(Repo.HTTPS_GITHUB_COM),
                        url.startswith(Repo.HTTPS_GITLAB_COM)], "Repository should be on bitbucket.org, " \
                                                                "foss.heptapod.net, github.com, or gitlab.com."
        assert re.search(r"^https://(github\.com|gitlab\.com|bitbucket\.org|foss\.heptapod\.net)/[^/]+/[^/]+", url), \
            "url is not a repository"

    def _derive_api(self):
        if self.platform == Platform.BITBUCKET:
            return "https://api.bitbucket.org/2.0/repositories/{0}/{1}".format(self.owner, self.repo)
        if self.platform == Platform.GITHUB:
            return "https://api.github.com/repos/{0}/{1}".format(self.owner, self.repo)
        if self.platform == Platform.GITLAB:
            return "https://gitlab.com/api/v4/projects/{0}%2F{1}".format(self.owner, self.repo)
        if self.platform == Platform.HEPTAPOD:
            return "https://foss.heptapod.net/api/v4/projects/{0}%2F{1}".format(self.owner, self.repo)
        raise ValueError("Unsupported URL: URL does not match any of the supported source control platforms")

    def _derive_owner_and_repo(self):
        if self.platform == Platform.BITBUCKET:
            try:
                owner, repo = self.url.replace(Repo.HTTPS_BITBUCKET_ORG, "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e

        if self.platform == Platform.GITHUB:
            try:
                owner, repo = self.url.replace(Repo.HTTPS_GITHUB_COM, "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e

        if self.platform == Platform.GITLAB:
            try:
                owner, repo = self.url.replace(Repo.HTTPS_GITLAB_COM, "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e

        if self.platform == Platform.HEPTAPOD:
            try:
                owner, repo = self.url.replace(Repo.HTTPS_FOSS_HEPTAPOD_NET, "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e

        if owner == "" or repo == "":
            raise ValueError("Bad value for input argument URL.")

        return owner, repo

    def _derive_platform(self):
        if self.url.startswith(Repo.HTTPS_BITBUCKET_ORG):
            return Platform.BITBUCKET

        if self.url.startswith(Repo.HTTPS_GITHUB_COM):
            return Platform.GITHUB

        if self.url.startswith(Repo.HTTPS_GITLAB_COM):
            return Platform.GITLAB

        if self.url.startswith(Repo.HTTPS_FOSS_HEPTAPOD_NET):
            return Platform.HEPTAPOD

        return None

    def _derive_raw_url_format_string(self):
        if self.branch is not None:
            # User specified a branch, use that regardless of whether it actually exists
            branch = self.branch
        else:
            branch = self.default_branch

        if self.platform == Platform.BITBUCKET:
            return "https://bitbucket.org/{0}/{1}/raw/{2}{3}" \
                   .format(self.owner, self.repo, branch, self.path) + "/{0}"

        if self.platform == Platform.GITHUB:
            return "https://raw.githubusercontent.com/{0}/{1}/{2}{3}" \
                   .format(self.owner, self.repo, branch, self.path) + "/{0}"

        if self.platform == Platform.GITLAB:
            return "https://gitlab.com/{0}/{1}/-/raw/{2}{3}" \
                   .format(self.owner, self.repo, branch, self.path) + "/{0}"

        if self.platform == Platform.HEPTAPOD:
            return "https://foss.heptapod.net/{0}/{1}/-/raw/{2}{3}" \
                   .format(self.owner, self.repo, branch, self.path) + "/{0}"

        raise ValueError("Unsupported URL: URL does not match any of the supported source control platforms")

    def _get_default_branch(self):
        fallback_branch = "main"
        response = requests.get(self.api)

        # If the request was successful, the next line will not raise any Exception
        try:
            response.raise_for_status()
        except requests.HTTPError:
            return fallback_branch

        if self.platform == Platform.BITBUCKET:
            return response.json().get("mainbranch", {"name": fallback_branch}).get("name")

        if self.platform in [Platform.GITLAB, Platform.GITHUB, Platform.HEPTAPOD]:
            return response.json().get("default_branch", fallback_branch)

        return None
