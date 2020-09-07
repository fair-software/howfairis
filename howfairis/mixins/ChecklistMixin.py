import re


class ChecklistMixin:
    def has_core_infrastructures_badge(self):
        if self.readme is None:
            self.print_state(check_name="has_core_infrastructures_badge", state=False)
            return False
        regex = r"!\[.*\]\(https://bestpractices\.coreinfrastructure\.org" + \
                r"/projects/[0-9]*/badge\)\]\(https://bestpractices\." + \
                r"coreinfrastructure\.org/projects/[0-9]*\)"
        r = re.compile(regex).search(self.readme) is not None
        self.print_state(check_name="has_core_infrastructures_badge", state=r)
        return r

    def has_sonarcloud_badge(self):
        if self.readme is None:
            self.print_state(check_name="has_sonarcloud_badge", state=False)
            return False
        regex = r"!\[.*\]\(https://sonarcloud\.io/api/project_badges/.*\)\]" + \
                r"\(https://sonarcloud\.io/dashboard\?id=.*\)"
        r = re.compile(regex).search(self.readme) is not None
        self.print_state(check_name="has_sonarcloud_badge", state=r)
        return r
