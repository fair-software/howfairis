from urllib.parse import quote
from .readme_format import ReadmeFormat


# pylint: disable=too-many-arguments
class Compliance:
    """Compliance of a repo against the 5 FAIR software recommendations

    Attributes:
        repository: Whether repository is publicly accessible with version control
        repo_license: Whether repository has a license
        registry: Whether code is in a registry
        citation: Whether software is citable
        checklist: Whether a software quality checklist is used
        compliant_symbol: Unicode symbol used in badge when compliant
        noncompliant_symbol: Unicode symbol used in badge when non-compliant
    """

    COMPLIANT_SYMBOL = "\u25CF"
    NONCOMPLIANT_SYMBOL = "\u25CB"

    def __init__(self, repository=False, repo_license=False, registry=False, citation=False, checklist=False):
        self._index = 0
        self.checklist = checklist
        self.citation = citation
        self.repo_license = repo_license
        self.registry = registry
        self.repository = repository

    def __eq__(self, other):
        return isinstance(other, Compliance) and [s is o for s, o in zip(self._state, other._state)] == [True] * 5

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
        return [self.repository, self.repo_license, self.registry,
                self.citation, self.checklist]

    def as_unicode(self):
        """String representation of each 5 recommendations.
        Where a full dot means compliant with the recommendation and a open dot means not-compliant.

        Returns: A string
        """
        compliance_unicode = [None] * 5
        for i, c in enumerate(self._state):
            if c is True:
                compliance_unicode[i] = Compliance.COMPLIANT_SYMBOL
            else:
                compliance_unicode[i] = Compliance.NONCOMPLIANT_SYMBOL
        return compliance_unicode

    def calc_badge(self, readme_file_format):
        score = self.count(True)

        if score in [0, 1]:
            color_string = "red"
        elif score in [2, 3]:
            color_string = "orange"
        elif score in [4]:
            color_string = "yellow"
        elif score == 5:
            color_string = "green"

        badge_url = "https://img.shields.io/badge/fair--software.eu-{0}-{1}".format(self.urlencode(), color_string)
        if readme_file_format == ReadmeFormat.RESTRUCTUREDTEXT:
            return ".. image:: {0}\n   :target: {1}".format(badge_url, "https://fair-software.eu")
        if readme_file_format == ReadmeFormat.MARKDOWN:
            return "[![fair-software.eu]({0})]({1})".format(badge_url, "https://fair-software.eu")

        return None

    def count(self, value=True):
        return self._state.count(value)

    def urlencode(self, separator="%20%20"):
        return separator.join([quote(symbol) for symbol in self.as_unicode()])
