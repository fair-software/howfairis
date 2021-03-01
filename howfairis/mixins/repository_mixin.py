import requests
from howfairis.requesting.get_from_platform import get_from_platform
from ..code_repository_platforms import Platform


class RepositoryMixin:

    def check_repository(self):
        if not self.is_quiet:
            print("(1/5) repository")
        reason = self.skip_repository_checks_reason
        if reason is None:
            results = [self.has_open_repository()]
            return True in results
        if reason == "":
            if not self.is_quiet:
                self._print_state(check_name="skipped (no reason provided)", state=True)
            return True
        if not self.is_quiet:
            self._print_state(check_name="skipped (reason: {0})".format(reason), state=True)
        return True

    def has_open_repository(self):

        if self.repo.platform == Platform.GITHUB:
            url = self.repo.api
        elif self.repo.platform == Platform.GITLAB:
            url = self.repo.api + "/repository/tree"

        try:
            response = get_from_platform(self.repo.platform, url, "api", apikeys=self._apikeys)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError:
            self._print_state(check_name="has_open_repository", state=False)
            return False
        self._print_state(check_name="has_open_repository", state=True)
        return True
