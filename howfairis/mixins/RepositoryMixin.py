import requests


class RepositoryMixin:

    def has_open_repository(self):
        url = "https://api.github.com/repos/{0}/{1}".format(self.owner, self.repo)

        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self.print_state(check_name="has_open_repository", state=False)
            return False
        except Exception as err:
            print(f"Other error occurred: {err}")
        self.print_state(check_name="has_open_repository", state=True)
        return True
