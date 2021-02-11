import requests
from howfairis.code_repository_platforms import Platform


class RepositoryMixin:

    def check_repository(self):
        print("(1/5) repository:")
        reason = self.skip_repository_checks_reason
        if isinstance(reason, str):
            if reason == "":
                self._print_state(check_name="skipped without reason", state=True)
            else:
                self._print_state(check_name="skipped with reason: {0}".format(reason), state=True)
            results = [True]
        if reason is None:
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
