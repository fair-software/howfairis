import requests
from bs4 import BeautifulSoup
from howfairis.Platform import Platform


class LicenseMixin:

    def check_license(self):
        force_state = self.config.merged.get("force_license")
        if force_state not in [True, False, None]:
            raise ValueError("Unexpected configuration value for force.license.")
        if isinstance(force_state, bool):
            print("(2/5) license: force {0}".format(force_state))
            return force_state
        print("(2/5) license")
        results = [self.has_license()]
        return True in results

    def has_license(self):

        r = False

        if self.repo.platform == Platform.GITHUB:
            url = self.repo.api + "/license"
            try:
                response = requests.get(url)
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                self._print_state(check_name="has_license", state=r)
                return r
            r = True

        if self.repo.platform == Platform.GITLAB:
            url = "https://gitlab.com/{0}/{1}".format(self.repo.owner, self.repo.repo)

            try:
                response = requests.get(url)
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                self._print_state(check_name="has_license", state=r)
                return r

            r = BeautifulSoup(response.text, "html.parser") \
                .find("div", class_="project-buttons")\
                .find(string="No license. All rights reserved") is None

        self._print_state(check_name="has_license", state=r)
        return r
