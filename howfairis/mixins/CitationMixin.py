import requests


class CitationMixin:

    def check_citation(self):
        force = self.config.get("force", dict())
        if not isinstance(force, dict):
            force = dict()
        force_state = force.get("citation")
        if force_state not in [True, False, None]:
            raise ValueError("Unexpected configuration value for force.citation.")
        if isinstance(force_state, bool):
            print("(4/5) citation: force {0}".format(force_state))
            return force_state
        print("(4/5) citation")
        results = [
            self.has_citation_file(),
            self.has_citationcff_file(),
            self.has_codemeta_file(),
            self.has_zenodo_badge(),
            self.has_zenodo_metadata_file()
        ]
        return True in results

    def has_citation_file(self):
        url = "https://raw.githubusercontent.com/" + \
              "{0}/{1}/{2}/{3}/CITATION".format(self.owner, self.repo, self.branch, self.path)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_citation_file", state=False)
            return False
        self._print_state(check_name="has_citation_file", state=True)
        return True

    def has_citationcff_file(self):
        url = "https://raw.githubusercontent.com/" + \
              "{0}/{1}/{2}/CITATION.cff".format(self.owner, self.repo, self.branch)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_citationcff_file", state=False)
            return False
        self._print_state(check_name="has_citationcff_file", state=True)
        return True

    def has_codemeta_file(self):
        url = "https://raw.githubusercontent.com/" + \
              "{0}/{1}/{2}/codemeta.json".format(self.owner, self.repo, self.branch)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_codemeta_file", state=False)
            return False
        self._print_state(check_name="has_codemeta_file", state=True)
        return True

    def has_zenodo_badge(self):
        regexes = [r"https://zenodo\.org/badge/DOI/10\.5281/zenodo\.[0-9]*\.svg",
                   r"https://zenodo\.org/badge/[0-9]*\.svg"]
        return self._eval_regexes(regexes)

    def has_zenodo_metadata_file(self):
        url = "https://raw.githubusercontent.com/" + \
              "{0}/{1}/{2}/.zenodo.json".format(self.owner, self.repo, self.branch)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_zenodo_metadata_file", state=False)
            return False
        self._print_state(check_name="has_zenodo_metadata_file", state=True)
        return True
