import requests
from howfairis.Platform import Platform


class RepositoryMixin:

    def check_repository(self):
        force_state = self.config.merged.get("force_repository")
        if force_state not in [True, False, None]:
            raise ValueError("Unexpected configuration value for force.repository.")
        if isinstance(force_state, bool):
            print("(1/5) repository: force {0}".format(force_state))
            return force_state
        print("(1/5) repository")
        results = [self.has_open_repository()]
        return True in results

    def has_open_repository(self):

        if self.repo.platform == Platform.GITHUB:
            url = self.repo.api
        elif self.repo.platform == Platform.GITLAB:
            url = self.repo.api + "/repository/tree"

        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_open_repository", state=False)
            return False
        self._print_state(check_name="has_open_repository", state=True)
        return True
