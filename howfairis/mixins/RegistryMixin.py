import re
import requests


class RegistryMixin:
    def has_pypi_badge(self):
        if self.readme is None:
            self.print_state(check_name="has_pypi_badge", state=False)
            return False
        regex = r"!\[.*\]\(https://img\.shields\.io/pypi/v/[^.]*\.svg.*\)\]" + \
                r"\(https://pypi\.python\.org/pypi/.*\)"
        r = re.compile(regex).search(self.readme) is not None
        self.print_state(check_name="has_pypi_badge", state=r)
        return r

    def has_bintray_badge(self):
        if self.readme is None:
            self.print_state(check_name="has_bintray_badge", state=False)
            return False
        regex = r"!\[.*\]\(https://api\.bintray\.com/packages" + \
                r"/.*/.*/.*/images/download\.svg\)\]" + \
                r"\(https://bintray\.com/.*/.*/.*/.*\)"
        r = re.compile(regex).search(self.readme) is not None
        self.print_state(check_name="has_bintray_badge", state=r)
        return r

    def has_conda_badge(self):
        if self.readme is None:
            self.print_state(check_name="has_conda_badge", state=False)
            return False
        regex = r"!\[.*\]\(https://anaconda\.org/.*/.*/badges" + \
                r"/installer/conda\.svg\)\]" + \
                r"\(https://anaconda\.org/.*/.*\)"
        r = re.compile(regex).search(self.readme) is not None
        self.print_state(check_name="has_conda_badge", state=r)
        return r

    def is_on_github_marketplace(self):
        try:
            response = requests.get(self.url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            self.print_state(check_name="is_on_github_marketplace", state=False)
            return False
        except Exception as err:
            print(f"Other error occurred: {err}")

        html = response.text
        r = "Use this GitHub Action with your project" in html and \
            "Add this Action to an existing workflow or create a new one." in html
        self.print_state(check_name="is_on_github_marketplace", state=r)
        return r
