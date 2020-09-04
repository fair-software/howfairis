import sys

from howfairis.check_checklist import main as check_checklist
from howfairis.check_license import main as check_license
from howfairis.check_registry import main as check_registry
from howfairis.check_repository import main as check_repository


class HowFairIsChecker:
    def __init__(self, url):
        self.url = url
        self.repository_is_compliant = None
        self.license_is_compliant = None
        self.registry_is_compliant = None
        self.citation_is_compliant = None
        self.checklist_is_compliant = None
        self.badge = None

    def check_repository(self):
        self.repository_is_compliant = check_repository()
        return self

    def check_license(self):
        self.license_is_compliant = check_license()
        return self

    def check_registry(self):
        self.registry_is_compliant = check_registry()
        return self

    def check_citation(self):
        print("citation checks SKIPPED")
        return self

    def check_checklist(self):
        self.checklist_is_compliant = check_checklist()
        return self

    def check_badge(self):

        compliance = [self.repository_is_compliant,
                      self.license_is_compliant,
                      self.registry_is_compliant,
                      self.citation_is_compliant,
                      self.checklist_is_compliant]

        compliant_symbol = "%E2%97%8F"
        noncompliant_symbol = "%E2%97%8B"
        compliance_string = "%20".join([compliant_symbol if c is True else noncompliant_symbol for c in compliance])
        score = compliance_string.count(compliant_symbol)
        if score in [0, 1]:
            color_string = "red"
        elif score in [2, 3, 4]:
            color_string = "orange"
        elif score == 5:
            color_string = "green"

        self.badge = "![fair-software.eu](https://img.shields.io/badge/fair--software.eu-{0}-{1})".format(compliance_string, color_string)

        # this string should be retrieved from the repo in the future:
        readme_string = "sdlfnsdnfsdnf ![fair-software.eu](https://img.shields.io/badge/fair--software.eu-" +\
                        "%E2%97%8B%20%E2%97%8B%20%E2%97%8B%20%E2%97%8B%20%E2%97%8B-red) a sdnfk anjsdfkj adnfkj " +\
                        " abnsdfibuweifkj xzkcijbsdi"

        if readme_string.find(self.badge) == -1:
            print("\nWhile searching through your README.md, I did not find the expected badge:\n" + self.badge + "\n")
            sys.exit(1)
        else:
            print("\nExpected badge is equal to the actual badge. It's all good.\n")
            sys.exit(0)


def main():
    print("Checking compliance with fair-software.eu...")
    
    if len(sys.argv) != 2:
        raise Exception("Expected exactly one argument, i.e. the URL for which GitHub repository to run the analysis.")

    url = sys.argv[1]
    print('Running for {0}'.format(url))
    checker = HowFairIsChecker(url)
    checker.check_repository()
    checker.check_license()
    checker.check_registry()
    checker.check_citation()
    checker.check_checklist()
    checker.check_badge()


if __name__ == "__main__":
    main()
