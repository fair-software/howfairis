class ChecklistMixin:

    def check_checklist(self):
        force = self.config.get("force", dict())
        if not isinstance(force, dict):
            force = dict()
        force_state = force.get("checklist")
        if force_state not in [True, False, None]:
            raise ValueError("Unexpected configuration value for force.checklist.")
        if isinstance(force_state, bool):
            print("(5/5) checklist: force {0}".format(force_state))
            return force_state
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
