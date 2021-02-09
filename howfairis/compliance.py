from urllib.parse import quote

from howfairis.readme_format import ReadmeFormat


# pylint: disable=too-many-arguments
class Compliance:
    """Compliance of a repo against the 5 FAIR software recommendations

    Attributes:
        repository (bool): Whether repository is publicly accessible with version control
        license (bool): Whether repository has a license
        registry (bool): Whether code is in a registry
        citation (bool): Whether software is citable
        checklist (bool): Whether a software quality checklist is used
        compliant_symbol (str): Unicode symbol used in badge when compliant
        noncompliant_symbol (str): Unicode symbol used in badge when non-compliant
    """

    def __init__(self, repository: bool = False, license_: bool = False, registry: bool = False,
                 citation: bool = False, checklist: bool = False,
                 compliant_symbol: str = "\u25CF", noncompliant_symbol: str = "\u25CB"):
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

        Returns: A list of string
        """
        compliance_unicode = [None] * 5
        for i, c in enumerate(self._state):
            if c is True:
                compliance_unicode[i] = self.compliant_symbol
            else:
                compliance_unicode[i] = self.noncompliant_symbol
        return compliance_unicode

    def calc_badge(self, fmt: ReadmeFormat) -> str:
        """Compute FAIR software badge image URL and URL in format of README.

        Args:
            fmt: Format of README

        Returns:
            Badge image link

        Raises:
            ValueError: If fmt is unknown
        """
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
        raise ValueError('Unable to calculate badge: unknown format')

    def count(self, value: bool) -> int:
        """Number of recommendations that have given value

        Args:
            value: If True then returns number of recommendations that are compliant

        Returns:
            Number of recommendations that have given value
        """
        return self._state.count(value)

    def urlencode(self, separator="%20%20"):
        return separator.join([quote(symbol) for symbol in self.as_unicode()])
