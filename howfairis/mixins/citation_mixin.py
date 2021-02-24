import requests
from howfairis.requesting.get_from_platform import get_from_platform


class CitationMixin:

    def check_citation(self):
        if not self.is_quiet:
            print("(4/5) citation")
        reason = self.skip_citation_checks_reason
        if reason is None:
            results = [
                self.has_citation_file(),
                self.has_citationcff_file(),
                self.has_codemeta_file(),
                self.has_zenodo_badge(),
                self.has_zenodo_metadata_file()
            ]
            return True in results
        if reason == "":
            self._print_state(check_name="skipped (no reason provided)", state=True)
            return True
        self._print_state(check_name="skipped (reason: {0})".format(reason), state=True)
        return True

    def has_citation_file(self):
        url = self.repo.raw_url_format_string.format("CITATION")
        try:
            response = get_from_platform(self.repo.platform, url, "raw", apikeys=self._apikeys)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_citation_file", state=False)
            return False
        self._print_state(check_name="has_citation_file", state=True)
        return True

    def has_citationcff_file(self):
        url = self.repo.raw_url_format_string.format("CITATION.cff")
        try:
            response = get_from_platform(self.repo.platform, url, "raw", apikeys=self._apikeys)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_citationcff_file", state=False)
            return False
        self._print_state(check_name="has_citationcff_file", state=True)
        return True

    def has_codemeta_file(self):
        url = self.repo.raw_url_format_string.format("codemeta.json")
        try:
            response = get_from_platform(self.repo.platform, url, "raw", apikeys=self._apikeys)
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
        url = self.repo.raw_url_format_string.format(".zenodo.json")
        try:
            response = get_from_platform(self.repo.platform, url, "raw", apikeys=self._apikeys)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_zenodo_metadata_file", state=False)
            return False
        self._print_state(check_name="has_zenodo_metadata_file", state=True)
        return True
