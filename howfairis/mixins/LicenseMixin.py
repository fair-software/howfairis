import requests


class LicenseMixin:

    def check_license(self):
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
            self.print_state(check_name="has_license", state=False)
            return False
        self.print_state(check_name="has_license", state=True)
        return True
