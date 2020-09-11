class ChecklistMixin:

    def check_checklist(self):
        print("(5/5) checklist")
        results = [
            self.has_core_infrastructures_badge(),
            self.has_sonarcloud_badge()
        ]
        return True in results

    def has_core_infrastructures_badge(self):
        regexes = [r"https://bestpractices\.coreinfrastructure\.org/projects/[0-9]*/badge"]
        return self._eval_regexes(regexes)

    def has_sonarcloud_badge(self):
        regexes = [r"https://sonarcloud\.io/api/project_badges/.*",
                   r"https://sonarcloud\.io/dashboard\?id=.*"]
        return self._eval_regexes(regexes)
