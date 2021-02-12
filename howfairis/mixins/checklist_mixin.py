class ChecklistMixin:

    def check_checklist(self):
        print("(5/5) checklist:")
        reason = self.skip_checklist_checks_reason
        if isinstance(reason, str):
            if reason == "":
                self._print_state(check_name="skipped (no reason provided)", state=True)
            else:
                self._print_state(check_name="skipped (reason: {0})".format(reason), state=True)
            results = [True]
        if reason is None:
            results = [self.has_core_infrastructures_badge()]
        return True in results

    def has_core_infrastructures_badge(self):
        regexes = [r"https://bestpractices\.coreinfrastructure\.org/projects/[0-9]*/badge"]
        return self._eval_regexes(regexes)
