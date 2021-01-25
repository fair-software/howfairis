from .Platform import Platform


class Repo:
    def __init__(self, url, branch=None, path=None, config_file=None):
        # run assertions on user input
        Repo._check_assertions(url)

        # assign arguments to instance members
        self.url = url
        self.branch = branch
        self.path = "" if path is None else "/" + path.strip("/")
        self.config_file = config_file

        # assign remaining members as needed
        self.platform = self._derive_platform()
        self.default_branch = self._set_default_branch()
        self.owner, self.repo = self._derive_owner_and_repo()

        # construct raw_url and api url
        self.api, self.raw_url_format_string = self._construct_urls()

    def _check_assertions(url):
        assert url.startswith("https://"), "url should start with https://"
        assert True in [url.startswith("https://github.com"),
                        url.startswith("https://gitlab.com")], "Repository should be on github.com or on gitlab.com."

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

    def _set_default_branch(self):
        if self.platform == Platform.GITHUB:
            return "master"
        if self.platform == Platform.GITLAB:
            return "master"
        return None

    def _derive_platform(self):
        if self.url.startswith("https://github.com"):
            return Platform.GITHUB
        if self.url.startswith("https://gitlab.com"):
            return Platform.GITLAB
        return None

    def _construct_urls(self):
        if self.platform == Platform.GITHUB:
            api = "https://api.github.com/repos/{0}/{1}".format(self.owner, self.repo)
            raw_url_format_string = "https://raw.githubusercontent.com/{0}/{1}/{2}{3}" \
                                    .format(self.owner, self.repo, self.branch, self.path) + "/{0}"

        elif self.platform == Platform.GITLAB:
            api = "https://gitlab.com/api/v4/projects/{0}%2F{1}".format(self.owner, self.repo)
            raw_url_format_string = "https://gitlab.com/{0}/{1}/-/raw/{2}{3}" \
                                    .format(self.owner, self.repo, self.branch, self.path) + "/{0}"

        return api, raw_url_format_string
