from .Platform import Platform


class Repo:
    def __init__(self, url, branch=None, path=None, config_file=None):
        self.api = None
        self.branch = "master" if branch is None else branch
        self.config_file = config_file
        self.owner = None
        self.path = "" if path is None else "/" + path.strip("/")
        self.platform = None
        self.raw_url_format_string = None
        self.repo = None
        self.url = url

        self._deconstruct_url()

    def _deconstruct_url(self):

        assert self.url.startswith("https://"), "url should start with https://"
        assert True in [self.url.startswith("https://github.com"),
                        self.url.startswith("https://gitlab.com")], "Repository should be on GitHub or on GitLab."

        if self.url.startswith("https://github.com"):
            self.platform = Platform.GITHUB
            try:
                self.owner, self.repo = self.url.replace("https://github.com", "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e
            self.raw_url_format_string = "https://raw.githubusercontent.com/{0}/{1}/{2}{3}" \
                                         .format(self.owner, self.repo, self.branch, self.path) + "/{0}"
            self.api = "https://api.github.com/repos/{0}/{1}".format(self.owner, self.repo)

        elif self.url.startswith("https://gitlab.com"):
            self.platform = Platform.GITLAB
            try:
                self.owner, self.repo = self.url.replace("https://gitlab.com", "").strip("/").split("/")[:2]
            except ValueError as e:
                raise ValueError("Bad value for input argument URL.") from e
            self.raw_url_format_string = "https://gitlab.com/{0}/{1}/-/raw/{2}{3}" \
                                         .format(self.owner, self.repo, self.branch, self.path) + "/{0}"
            self.api = "https://gitlab.com/api/v4/projects/{0}%2F{1}".format(self.owner, self.repo)

        if self.owner == "" or self.repo == "":
            raise ValueError("Bad value for input argument URL.")

        return self
