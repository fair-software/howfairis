import requests
from howfairis.requesting.get_from_platform import get_from_platform
from ..code_repository_platforms import Platform


class RegistryMixin:

    def check_registry(self):
        if not self.is_quiet:
            print("(3/5) registry")
        reason = self.skip_registry_checks_reason
        if reason is None:
            results = [
                self.has_ascl_badge(),
                self.has_bintray_badge(),
                self.has_conda_badge(),
                self.has_cran_badge(),
                self.has_crates_badge(),
                self.has_maven_badge(),
                self.has_npm_badge(),
                self.has_pypi_badge(),
                self.has_rsd_badge(),
                self.is_on_github_marketplace()
            ]
            return True in results
        if reason == "":
            if not self.is_quiet:
                self._print_state(check_name="skipped (no reason provided)", state=True)
            return True
        if not self.is_quiet:
            self._print_state(check_name="skipped (reason: {0})".format(reason), state=True)
        return True

    def has_ascl_badge(self):
        regexes = [r"https://img\.shields\.io/badge/ascl.*"]
        return self._eval_regexes(regexes)

    def has_bintray_badge(self):
        regexes = [r"https://api\.bintray\.com/packages/.*/.*/.*/images/download\.svg",
                   r"https://img\.shields\.io/bintray/.*"]
        return self._eval_regexes(regexes)

    def has_conda_badge(self):
        regexes = [r"https://anaconda\.org/.*/.*/badges/downloads\.svg",
                   r"https://anaconda\.org/.*/.*/badges/installer/conda\.svg",
                   r"https://anaconda\.org/.*/.*/badges/latest_release_date\.svg",
                   r"https://anaconda\.org/.*/.*/badges/latest_release_relative_date\.svg",
                   r"https://anaconda\.org/.*/.*/badges/platforms\.svg",
                   r"https://anaconda\.org/.*/.*/badges/version\.svg",
                   r"https://img\.shields\.io/conda/.*"]
        return self._eval_regexes(regexes)

    def has_cran_badge(self):
        regexes = [r"https://cranlogs\.r-pkg\.org/badges/.*",
                   r"https://www\.r-pkg\.org/badges/.*",
                   r"https://img\.shields\.io/cran/.*"]
        return self._eval_regexes(regexes)

    def has_crates_badge(self):
        regexes = [r"https://badgen.net/crates/v/.*",
                   r"https://img\.shields\.io/crates/.*"]
        return self._eval_regexes(regexes)

    def has_maven_badge(self):
        regexes = [r"https://badgen.net/maven/v/maven-central/.*",
                   r"https://img\.shields\.io/maven-central/.*",
                   r"https://img\.shields\.io/maven-metadata/.*"]
        return self._eval_regexes(regexes)

    def has_npm_badge(self):
        regexes = [r"https://badge.fury.io/js/.*",
                   r"https://badgen.net/npm/v/.*",
                   r"https://img\.shields\.io/npm/.*"]
        return self._eval_regexes(regexes)

    def has_pypi_badge(self):
        regexes = [r"https://pypi\.python\.org/pypi/",
                   r"https://badge\.fury\.io/py/.*\.svg",
                   r"https://badgen\.net/pypi/v/.*",
                   r"https://img\.shields\.io/pypi/.*"]
        return self._eval_regexes(regexes)

    def has_rsd_badge(self):
        regexes = [r"https://img\.shields\.io/badge/RSD-.*",
                   r"https://img\.shields\.io/badge/rsd-.*"]
        return self._eval_regexes(regexes)

    def is_on_github_marketplace(self):

        r = False

        if self.repo.platform == Platform.GITHUB:
            try:
                response = get_from_platform(self.repo.platform, self.repo.url, "frontend", apikeys=self._apikeys)
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                self._print_state(check_name="is_on_github_marketplace", state=r)
                return r

            html = response.text
            r = "Use this GitHub Action with your project" in html and \
                "Add this Action to an existing workflow or create a new one." in html

        self._print_state(check_name="is_on_github_marketplace", state=r)
        return r
