import requests


class LicenseMixin:

    def check_license(self):
        force = self.config.get("force", dict())
        if not isinstance(force, dict):
            force = dict()
        force_state = force.get("license")
        if force_state not in [True, False, None]:
            raise ValueError("Unexpected configuration value for force.license.")
        if isinstance(force_state, bool):
            print("(2/5) license: force {0}".format(force_state))
            return force_state
        print("(2/5) license")
        results = [self.has_license()]
        return True in results

    def has_license(self):
        url = "https://api.github.com/repos/{0}/{1}/license".format(self.owner, self.repo)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_license", state=False)
            return False
        self._print_state(check_name="has_license", state=True)
        return True
