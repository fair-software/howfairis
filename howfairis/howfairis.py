import sys
import requests
import re
from colorama import init as init_terminal_colors, Style, Fore


# # # # # # # # # # # # # # # # # # # # # #
#               repository                #
# # # # # # # # # # # # # # # # # # # # # #
def print_state(func_name="", state=None, indent=8):
    if state is True:
        print(" " * indent + func_name + ": " + Style.BRIGHT + Fore.GREEN + str(state).lower() + Style.RESET_ALL)
    elif state is False:
        print(" " * indent + func_name + ": " + str(state).lower())


def has_open_repository(owner, repo):
    url = "https://api.github.com/repos/{0}/{1}".format(owner, repo)

    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError:
        print_state(func_name="has_open_repository", state=False)
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")
    print_state(func_name="has_open_repository", state=True)
    return True


# # # # # # # # # # # # # # # # # # # # # #
#                license                  #
# # # # # # # # # # # # # # # # # # # # # #


def has_license(owner, repo):
    url = "https://api.github.com/repos/{0}/{1}/license".format(owner, repo)
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError:
        print_state(func_name="has_license", state=False)
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")
    print_state(func_name="has_license", state=True)
    return True


# # # # # # # # # # # # # # # # # # # # # #
#                registry                 #
# # # # # # # # # # # # # # # # # # # # # #


def has_pypi_badge(s):
    regex = r"!\[.*\]\(https://img\.shields\.io/pypi/v/[^.]*\.svg.*\)\]" + \
            r"\(https://pypi\.python\.org/pypi/.*\)"
    r = re.compile(regex).search(s) is not None
    print_state(func_name="has_pypi_badge", state=r)
    return r


def has_bintray_badge(s):
    regex = r"!\[.*\]\(https://api\.bintray\.com/packages" + \
            r"/.*/.*/.*/images/download\.svg\)\]" + \
            r"\(https://bintray\.com/.*/.*/.*/.*\)"
    r = re.compile(regex).search(s) is not None
    print_state(func_name="has_bintray_badge", state=r)
    return r


def has_conda_badge(s):
    regex = r"!\[.*\]\(https://anaconda\.org/.*/.*/badges" + \
            r"/installer/conda\.svg\)\]" + \
            r"\(https://anaconda\.org/.*/.*\)"
    r = re.compile(regex).search(s) is not None
    print_state(func_name="has_conda_badge", state=r)
    return r


def is_on_github_marketplace(url):
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print_state(func_name="is_on_github_marketplace", state=False)
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")

    html = response.text
    r = "Use this GitHub Action with your project" in html and \
        "Add this Action to an existing workflow or create a new one." in html
    print_state(func_name="has_bintray_badge", state=r)
    return r


# # # # # # # # # # # # # # # # # # # # # #
#                citation                 #
# # # # # # # # # # # # # # # # # # # # # #


def has_zenodo_badge(s):
    regex = r"!\[.*\]\(https://zenodo\.org/badge/DOI/10\.5281/zenodo" + \
            r"\.[0-9]*\.svg\)\]\(https://doi\.org/10\.5281/zenodo\.[0-9]*\)"
    r = re.compile(regex).search(s) is not None
    print_state(func_name="has_zenodo_badge", state=r)
    return r


def has_citation_file(owner, repo, branch="master"):
    url = "https://raw.githubusercontent.com/" + \
          "{0}/{1}/{2}/CITATION".format(owner, repo, branch)
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError:
        print_state(func_name="has_citation_file", state=False)
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")
    print_state(func_name="has_citation_file", state=True)
    return True


def has_citationcff_file(owner, repo, branch="master"):
    url = "https://raw.githubusercontent.com/" + \
          "{0}/{1}/{2}/CITATION.cff".format(owner, repo, branch)
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError:
        print_state(func_name="has_citationcff_file", state=False)
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")
    print_state(func_name="has_citationcff_file", state=True)
    return True


def has_zenodo_metadata_file(owner, repo, branch="master"):
    url = "https://raw.githubusercontent.com/" + \
          "{0}/{1}/{2}/.zenodo.json".format(owner, repo, branch)
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError:
        print_state(func_name="has_zenodo_metadata_file", state=False)
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")
    print_state(func_name="has_zenodo_metadata_file", state=True)
    return True


def has_codemeta_file(owner, repo, branch="master"):
    url = "https://raw.githubusercontent.com/" + \
          "{0}/{1}/{2}/codemeta.json".format(owner, repo, branch)
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError:
        print_state(func_name="has_codemeta_file", state=False)
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")
    print_state(func_name="has_codemeta_file", state=True)
    return True


# # # # # # # # # # # # # # # # # # # # # #
#                checklist                #
# # # # # # # # # # # # # # # # # # # # # #


def has_core_infrastructures_badge(s):
    regex = r"!\[.*\]\(https://bestpractices\.coreinfrastructure\.org" + \
            r"/projects/[0-9]*/badge\)\]\(https://bestpractices\." + \
            r"coreinfrastructure\.org/projects/[0-9]*\)"
    r = re.compile(regex).search(s) is not None
    print_state(func_name="has_core_infrastructures_badge", state=r)
    return r


def has_sonarcloud_badge(s):
    regex = r"!\[.*\]\(https://sonarcloud\.io/api/project_badges/.*\)\]" + \
            r"\(https://sonarcloud\.io/dashboard\?id=.*\)"
    r = re.compile(regex).search(s) is not None
    print_state(func_name="has_sonarcloud_badge", state=r)
    return r


class HowFairIsChecker:
    def __init__(self, url):
        assert url.startswith("https://github.com/"), \
            "url should start with https://github.com"
        self.url = url
        self.readme = None
        self.repository_is_compliant = None
        self.license_is_compliant = None
        self.registry_is_compliant = None
        self.citation_is_compliant = None
        self.checklist_is_compliant = None
        self.badge = None
        self.owner = None
        self.repo = None
        self.readme_filename = None
        self.branch = None
        self.compliant_symbol = "\u25CF"
        self.noncompliant_symbol = "\u25CB"

    def check_badge(self):

        compliance_bool = [
            self.repository_is_compliant, self.license_is_compliant,
            self.registry_is_compliant, self.citation_is_compliant,
            self.checklist_is_compliant
        ]

        compliance_unicode = [None] * 5
        for i, c in enumerate(compliance_bool):
            if c is True:
                compliance_unicode[i] = self.compliant_symbol
            else:
                compliance_unicode[i] = self.noncompliant_symbol

        compliance_string = "%20%20".join(
            [requests.utils.quote(symbol) for symbol in compliance_unicode])

        score = compliance_bool.count(True)
        if score in [0, 1]:
            color_string = "red"
        elif score in [2, 3, 4]:
            color_string = "orange"
        elif score == 5:
            color_string = "green"

        self.badge = "![fair-software.eu](https://img.shields.io" + \
                     "/badge/fair--software.eu-{0}-{1})" \
                     .format(compliance_string, color_string)

        print("\nCalculated compliance: " + " ".join(compliance_unicode) + "\n")

        if self.readme is None:
            sys.exit(1)
        elif self.readme.find(self.badge) == -1:
            print("While searching through your README.md, I" +
                  " did not find the expected badge:\n" + self.badge + "\n")
            sys.exit(1)
        else:
            print("Expected badge is equal to the actual badge. " +
                  "It's all good.\n")
            sys.exit(0)

    def check_checklist(self):
        print("(5/5) checklist")
        if self.repository_is_compliant is False:
            self.checklist_is_compliant = False
            return self
        results = [
            has_core_infrastructures_badge(self.readme),
            has_sonarcloud_badge(self.readme)
        ]
        self.checklist_is_compliant = True in results
        return self

    def check_citation(self):
        print("(4/5) citation")
        if self.repository_is_compliant is False:
            self.citation_is_compliant = False
            return self
        results = [
            has_zenodo_badge(self.readme),
            has_citationcff_file(self.owner, self.repo, self.branch),
            has_citation_file(self.owner, self.repo, self.branch),
            has_zenodo_metadata_file(self.owner, self.repo, self.branch),
            has_codemeta_file(self.owner, self.repo, self.branch)
        ]
        self.citation_is_compliant = True in results
        return self

    def check_license(self):
        print("(2/5) license")
        if self.repository_is_compliant is False:
            self.license_is_compliant = False
            return self
        results = [has_license(self.owner, self.repo)]
        self.license_is_compliant = True in results
        return self

    def check_registry(self):
        print("(3/5) registry")
        if self.repository_is_compliant is False:
            self.registry_is_compliant = False
            return self
        results = [
            has_pypi_badge(self.readme),
            has_conda_badge(self.readme),
            has_bintray_badge(self.readme),
            is_on_github_marketplace(self.url)
        ]
        self.registry_is_compliant = True in results
        return self

    def check_repository(self):
        print("(1/5) repository")
        results = [has_open_repository(self.owner, self.repo)]
        self.repository_is_compliant = True in results
        return self

    def deconstruct_url(self):
        self.owner, self.repo = self.url.replace("https://github.com/",
                                                 "").split("/")[:2]
        self.branch = "master"
        self.readme_filename = "README.md"
        return self

    def get_readme(self):
        # only github urls supported
        # only README.md supported

        raw_url = "https://raw.githubusercontent.com/" + \
                  "{0}/{1}/{2}/{3}".format(self.owner, self.repo,
                                           self.branch, self.readme_filename)
        try:
            response = requests.get(raw_url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return self
        except Exception as err:
            print(f"Other error occurred: {err}")

        self.readme = response.text
        return self


def main():

    init_terminal_colors()

    print("Checking compliance with fair-software.eu...")

    if len(sys.argv) != 2:
        raise Exception("Expected exactly one argument, i.e. the URL for " +
                        "which GitHub repository to run the analysis.")

    url = sys.argv[1]
    print("Running for {0}\n".format(url))
    checker = HowFairIsChecker(url)
    checker.deconstruct_url()
    checker.get_readme()
    checker.check_repository()
    checker.check_license()
    checker.check_registry()
    checker.check_citation()
    checker.check_checklist()
    checker.check_badge()


if __name__ == "__main__":
    main()
