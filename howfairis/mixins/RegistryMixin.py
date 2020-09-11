import requests


class RegistryMixin:

    def check_registry(self):
        force = self.config.get("force", dict())
        if not isinstance(force, dict):
            force = dict()
        force_state = force.get("registry")
        if force_state not in [True, False, None]:
            raise ValueError("Unexpected configuration value for force.registry.")
        if isinstance(force_state, bool):
            print("(3/5) registry: force {0}".format(force_state))
            return force_state
        print("(3/5) registry")
        results = [
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

    def has_bintray_badge(self):
        regexes = [r"https://api\.bintray\.com/packages/.*/.*/.*/images/download\.svg",
                   r"https://img\.shields\.io/bintray/.*"]
        return self._eval_regexes(regexes)

    def has_conda_badge(self):
        regexes = [r"https://anaconda\.org/.*/.*/badges/installer/conda\.svg",
                   r"https://img\.shields\.io/conda/.*"]
        return self._eval_regexes(regexes)

    def has_cran_badge(self):
        regexes = [r"https://cranlogs\.r-pkg\.org/badges/.*",
                   r"https://cranlogs\.r-pkg\.org/badges/grand-total/.*",
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
        try:
            response = requests.get(self.url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="is_on_github_marketplace", state=False)
            return False

        html = response.text
        r = "Use this GitHub Action with your project" in html and \
            "Add this Action to an existing workflow or create a new one." in html
        self._print_state(check_name="is_on_github_marketplace", state=r)
        return r
