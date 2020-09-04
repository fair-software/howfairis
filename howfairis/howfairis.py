import sys
import requests


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

    def check_badge(self):

        compliance = [
            self.repository_is_compliant, self.license_is_compliant,
            self.registry_is_compliant, self.citation_is_compliant,
            self.checklist_is_compliant
        ]

        compliant_symbol = "%E2%97%8F"
        noncompliant_symbol = "%E2%97%8B"
        compliance_string = "%20%20".join([
            compliant_symbol if c is True else noncompliant_symbol
            for c in compliance
        ])
        score = compliance_string.count(compliant_symbol)
        if score in [0, 1]:
            color_string = "red"
        elif score in [2, 3, 4]:
            color_string = "orange"
        elif score == 5:
            color_string = "green"

        self.badge = "![fair-software.eu](https://img.shields.io/badge/fair--software.eu-{0}-{1})" \
                     .format(compliance_string, color_string)

        if self.readme.find(self.badge) == -1:
            print("\nWhile searching through your README.md, I" +
                  " did not find the expected badge:\n" + self.badge + "\n")
            sys.exit(1)
        else:
            print("\nExpected badge is equal to the actual badge. " +
                  "It's all good.\n")
            sys.exit(0)

    def check_checklist(self):
        print("checklist checks TODO")
        return self

    def check_citation(self):
        print("citation checks TODO")
        return self

    def check_license(self):
        print("license checks TODO")
        return self

    def check_registry(self):
        print("registry checks TODO")
        return self

    def check_repository(self):
        print("repository checks TODO")
        return self

    def get_readme(self):
        # only github urls supported
        # only README.md supported
        owner, repo = self.url.replace("https://github.com/", "") \
                              .split("/")[:2]

        branch = "master"
        file = "README.md"
        raw_url = "https://raw.githubusercontent.com/" + \
                  "{0}/{1}/{2}/{3}.md".format(owner, repo, branch, file)
        try:
            response = requests.get(raw_url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

        self.readme = response.text
        return self


def main():
    print("Checking compliance with fair-software.eu...")

    if len(sys.argv) != 2:
        raise Exception("Expected exactly one argument, i.e. the URL for " +
                        "which GitHub repository to run the analysis.")

    url = sys.argv[1]
    print("Running for {0}".format(url))
    checker = HowFairIsChecker(url)
    checker.get_readme()       \
           .check_repository() \
           .check_license()    \
           .check_registry()   \
           .check_citation()   \
           .check_checklist()  \
           .check_badge()


if __name__ == "__main__":
    main()
