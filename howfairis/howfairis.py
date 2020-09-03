from howfairis.check_badge import main as check_badge
from howfairis.check_checklist import main as check_checklist
from howfairis.check_citation import main as check_citation
from howfairis.check_license import main as check_license
from howfairis.check_registry import main as check_registry
from howfairis.check_repository import main as check_repository


class HowFairIsChecker:
    def __init__(self):
        self.badge = None
        self.repository_is_compliant = None
        self.license_is_compliant = None
        self.registry_is_compliant = None
        self.citation_is_compliant = None
        self.checklist_is_compliant = None

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
        self.badge = check_badge()


def main():
    print("How fair is")
    checker = HowFairIsChecker()


if __name__ == "__main__":
    main()