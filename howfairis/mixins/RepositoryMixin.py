import requests
from howfairis.Platform import Platform


class RepositoryMixin:

    def check_repository(self):
        force = self.config.get("force", dict())
        if not isinstance(force, dict):
            force = dict()
        force_state = force.get("repository")
        if force_state not in [True, False, None]:
            raise ValueError("Unexpected configuration value for force.repository.")
        if isinstance(force_state, bool):
            print("(1/5) repository: force {0}".format(force_state))
            return force_state
        print("(1/5) repository")
        results = [self.has_open_repository()]
        return True in results

    def has_open_repository(self):

        if self.platform == Platform.GITHUB:
            url = "https://api.github.com/repos/{0}/{1}".format(self.owner, self.repo)
        elif self.platform == Platform.GITLAB:
            url = "https://gitlab.com/api/v4/projects/{0}%2F{1}/repository/tree".format(self.owner, self.repo)

        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_open_repository", state=False)
            return False
        self._print_state(check_name="has_open_repository", state=True)
        return True
