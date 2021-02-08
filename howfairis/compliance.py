from urllib.parse import quote
from howfairis.readme_format import ReadmeFormat


# pylint: disable=too-many-arguments
class Compliance:
    """Compliance of a repo against the 5 FAIR software recommendations

    Attributes:
        repository: Whether repository is publicly accessible with version control
        license: Whether repository has a license
        registry: Whether code is in a registry
        citation: Whether software is citable
        checklist: Whether a software quality checklist is used
        compliant_symbol: Unicode symbol used in badge when compliant
        noncompliant_symbol: Unicode symbol used in badge when non-compliant
    """

    def __init__(self, repository=False, license_=False, registry=False, citation=False, checklist=False,
                 compliant_symbol="\u25CF", noncompliant_symbol="\u25CB"):
        self._index = 0
        self.checklist = checklist
        self.citation = citation
        self.compliant_symbol = compliant_symbol
        self.license = license_
        self.noncompliant_symbol = noncompliant_symbol
        self.registry = registry
        self.repository = repository

    def __eq__(self, other):
        return self.count(True) == other.count(True)

    def __ge__(self, other):
        return self.count(True) >= other.count(True)

    def __gt__(self, other):
        return self.count(True) > other.count(True)

    def __le__(self, other):
        return self.count(True) <= other.count(True)

    def __ne__(self, other):
        return self.count(True) != other.count(True)

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

    def calc_badge(self, fmt):
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
        if fmt == ReadmeFormat.RESTRUCTUREDTEXT:
            return ".. image:: {0}\n   :target: {1}".format(badge_url, "https://fair-software.eu")
        if fmt == ReadmeFormat.MARKDOWN:
            return "[![fair-software.eu]({0})]({1})".format(badge_url, "https://fair-software.eu")

        return None

    def count(self, value):
        return self._state.count(value)

    def urlencode(self, separator="%20%20"):
        return separator.join([quote(symbol) for symbol in self.as_unicode()])
