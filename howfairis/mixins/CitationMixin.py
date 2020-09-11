import requests


class CitationMixin:

    def check_citation(self):
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
              "{0}/{1}/{2}/CITATION".format(self.owner, self.repo, self.branch)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self.print_state(check_name="has_citation_file", state=False)
            return False
        self.print_state(check_name="has_citation_file", state=True)
        return True

    def has_citationcff_file(self):
        url = "https://raw.githubusercontent.com/" + \
              "{0}/{1}/{2}/CITATION.cff".format(self.owner, self.repo, self.branch)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self.print_state(check_name="has_citationcff_file", state=False)
            return False
        self.print_state(check_name="has_citationcff_file", state=True)
        return True

    def has_codemeta_file(self):
        url = "https://raw.githubusercontent.com/" + \
              "{0}/{1}/{2}/codemeta.json".format(self.owner, self.repo, self.branch)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self.print_state(check_name="has_codemeta_file", state=False)
            return False
        self.print_state(check_name="has_codemeta_file", state=True)
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
            self.print_state(check_name="has_zenodo_metadata_file", state=False)
            return False
        self.print_state(check_name="has_zenodo_metadata_file", state=True)
        return True
