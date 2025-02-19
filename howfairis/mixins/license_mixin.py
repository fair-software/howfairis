import requests
from bs4 import BeautifulSoup
from howfairis.exceptions.external_api_exception import ExternalAPIException
from howfairis.requesting.get_from_external_api import get_from_external_no_auth_api
from howfairis.requesting.get_from_platform import get_from_platform
from ..code_repository_platforms import Platform


class LicenseMixin:
    """ """

    def check_license(self):
        """ """
        if not self.is_quiet:
            print("(2/5) license")
        reason = self.skip_license_checks_reason
        if reason is None:
            results = [self.has_license(), self.is_reuse_compliant()]
            return True in results
        if reason == "":
            self._print_state(check_name="skipped (no reason provided)", state=True)
            return True
        self._print_state(check_name=f"skipped (reason: {reason})", state=True)
        return True

    def has_license(self):
        """ """
        result = False

        if self.repo.platform == Platform.GITHUB:
            url = self.repo.api + "/license"
            try:
                response = get_from_platform(
                    self.repo.platform, url, "api", apikeys=self._apikeys
                )
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                self._print_state(check_name="has_license", state=result)
                return result
            result = True

        if self.repo.platform == Platform.GITLAB:
            url = f"https://gitlab.com/{self.repo.owner}/{self.repo.repo}"

            try:
                response = get_from_platform(
                    self.repo.platform, url, "frontend", apikeys=self._apikeys
                )
                # If the response was successful, no Exception will be raised
                response.raise_for_status()
            except requests.HTTPError:
                self._print_state(check_name="has_license", state=result)
                return result

            result = (
                response is not None
                and response.text is not None
                and BeautifulSoup(response.text, "html.parser") is not None
                and BeautifulSoup(response.text, "html.parser").find(
                    "div", class_="project-buttons"
                )
                is not None
                and BeautifulSoup(response.text, "html.parser")
                .find("div", class_="project-buttons")
                .find(string="No license. All rights reserved")
                is None
            )

        self._print_state(check_name="has_license", state=result)
        return result

    def is_reuse_compliant(self):
        """ """

        try:
            response = get_from_external_no_auth_api(self.repo.reuse_url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            # check if the repository is compliant
            if response.json()["status"] == "compliant":
                self._print_state(check_name="is_reuse_compliant", state=True)
                return True
        except requests.HTTPError:
            self._print_state(check_name="is_reuse_compliant", state=False)
            return False

        self._print_state(check_name="is_reuse_compliant", state=False)
        return False
