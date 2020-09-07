import re
import requests


class CitationMixin:
    def has_zenodo_badge(self):
        if self.readme is None:
            self.print_state(check_name="has_zenodo_badge", state=False)
            return False
        regex = r"!\[.*\]\(https://zenodo\.org/badge/DOI/10\.5281/zenodo" + \
                r"\.[0-9]*\.svg\)\]\(https://doi\.org/10\.5281/zenodo\.[0-9]*\)"
        r = re.compile(regex).search(self.readme) is not None
        self.print_state(check_name="has_zenodo_badge", state=r)
        return r

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
        except Exception as err:
            print(f"Other error occurred: {err}")
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
        except Exception as err:
            print(f"Other error occurred: {err}")
        self.print_state(check_name="has_citationcff_file", state=True)
        return True

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
        except Exception as err:
            print(f"Other error occurred: {err}")
        self.print_state(check_name="has_zenodo_metadata_file", state=True)
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
        except Exception as err:
            print(f"Other error occurred: {err}")
        self.print_state(check_name="has_codemeta_file", state=True)
        return True
