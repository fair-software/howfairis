import sys

from howfairis.check_checklist import main as check_checklist
from howfairis.check_citation import main as check_citation
from howfairis.check_license import main as check_license
from howfairis.check_registry import main as check_registry
from howfairis.check_repository import main as check_repository


class HowFairIsChecker:
    def __init__(self):
        self.repository_is_compliant = None
        self.license_is_compliant = None
        self.registry_is_compliant = None
        self.citation_is_compliant = None
        self.checklist_is_compliant = None
        self.badge = None

    def check_repository(self):
        self.repository_is_compliant = check_repository()

    def check_license(self):
        self.license_is_compliant = check_license()

    def check_registry(self):
        self.registry_is_compliant = check_registry()

    def check_citation(self):
        self.citation_is_compliant = check_citation()

    def check_checklist(self):
        self.checklist_is_compliant = check_checklist()

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

        self.badge = "https://img.shields.io/badge/fair--software.eu-{0}-{1}".format(compliance_string, color_string)

        readme_string = "sdlfnsdnfsdnf https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%E2%97%8F%20" +\
                        "%E2%97%8F%20%E2%97%8F%20%E2%97%8F-green a sdnfk anjsdfkj adnfkj   abnsdfibuweifkj xzk" +\
                        "cijbsdi"

        if readme_string.find(self.badge) == -1:
            print("Expected badge is equal to the actual badge. It's all good.")
            sys.exit(0)
        else:
            print("Expected badge value:\n" + self.badge + "\n")
            sys.exit(1)


def main():
    print("Checking compliance with fair-software.eu...")
    checker = HowFairIsChecker()
    checker.check_repository()
    checker.check_license()
    checker.check_registry()
    checker.check_citation()
    checker.check_checklist()


if __name__ == "__main__":
    main()
