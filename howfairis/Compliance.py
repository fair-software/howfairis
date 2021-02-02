import requests


# pylint: disable=too-many-arguments
class Compliance:
    """Compliance of a repo against the 5 FAIR software recommendations

    Attributes:
        repository: Whether repository is publicly accessible with version control
        license: Whether repository has a license
        registry: Whether code is in a registry
        citation: Whether software is citable
        checklist: Whether a software quality checklist is used
    """
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
        """String representation of each 5 recommendations.
        Where a full dot means compliant with the recommendation and a open dot means not-compliant.

        Returns: A string
        """
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

    def __eq__(self, other):
        return \
            self.repository == other.repository and \
            self.license == other.license and \
            self.registry == other.registry and \
            self.citation == other.citation and \
            self.checklist == other.checklist and \
            self.compliant_symbol == other.compliant_symbol and \
            self.noncompliant_symbol == other.noncompliant_symbol
