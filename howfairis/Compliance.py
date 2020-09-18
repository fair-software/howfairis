import requests


# pylint: disable=too-many-arguments
class Compliance:
    def __init__(self, repository=None, license_=None, registry=None, citation=None, checklist=None,
                 compliant_symbol="\u25CF", noncompliant_symbol="\u25CB"):
        self._index = 0
        self.repository = repository
        self.license = license_
        self.registry = registry
        self.citation = citation
        self.checklist = checklist
        self.compliant_symbol = compliant_symbol
        self.noncompliant_symbol = noncompliant_symbol

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 5:
            result = self._state[self._index]
            self._index += 1
            return result
        self._index = 0
        raise StopIteration

    @property
    def _state(self):
        return [self.repository, self.license, self.registry,
                self.citation, self.checklist]

    def as_unicode(self):
        compliance_unicode = [None] * 5
        for i, c in enumerate(self._state):
            if c is True:
                compliance_unicode[i] = self.compliant_symbol
            else:
                compliance_unicode[i] = self.noncompliant_symbol
        return compliance_unicode

    def count(self, value):
        return self._state.count(value)

    def urlencode(self):
        return "%20%20".join([requests.utils.quote(symbol) for symbol in self.as_unicode()])
