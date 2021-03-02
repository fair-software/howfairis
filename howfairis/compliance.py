from typing import Optional
from urllib.parse import quote
from .readme_format import ReadmeFormat


# pylint: disable=too-many-arguments
class Compliance:
    """Compliance of a repo against the 5 FAIR software recommendations

    Args:
        repository: Whether repository is publicly accessible with version control
        license_: Whether repository has a license
        registry: Whether code is in a registry
        citation: Whether software is citable
        checklist: Whether a software quality checklist is used

    Attributes:
        repository (bool): Whether repository is publicly accessible with version control
        license (bool): Whether repository has a license
        registry (bool): Whether code is in a registry
        citation (bool): Whether software is citable
        checklist (bool): Whether a software quality checklist is used
    """
    COMPLIANT_SYMBOL = "\u25CF"
    NONCOMPLIANT_SYMBOL = "\u25CB"

    def __init__(self, repository: bool = False, license_: bool = False, registry: bool = False,
                 citation: bool = False, checklist: bool = False):
        self._index = 0
        self.checklist = checklist
        self.citation = citation
        self.license = license_
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
        return [self.repository, self.license, self.registry,
                self.citation, self.checklist]

    def as_unicode(self) -> str:
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

    def calc_badge(self, readme_file_format: ReadmeFormat) -> Optional[str]:
        """Calculate FAIR software badge image URL and URL in format of README.

        Args:
            readme_file_format: Format of README.

        Returns:
            Badge image link or None when format of README is unsupported.
        """
        badge_url = self.badge_image_url()
        if readme_file_format == ReadmeFormat.RESTRUCTUREDTEXT:
            return ".. image:: {0}\n   :target: {1}".format(badge_url, "https://fair-software.eu")
        if readme_file_format == ReadmeFormat.MARKDOWN:
            return "[![fair-software.eu]({0})]({1})".format(badge_url, "https://fair-software.eu")

        return None

    def badge_image_url(self) -> str:
        """FAIR software badge image URL"""
        color_string = self.color()
        compliance_string = self.urlencode()
        return "https://img.shields.io/badge/fair--software.eu-{0}-{1}".format(compliance_string, color_string)

    def color(self) -> str:
        """Traffic light color for badge based on compliance count

        Returns:
            CSS friendly color name
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
        return color_string

    def count(self, value=True) -> int:
        """Number of recommendations which are compliant or non-compliant

        Args:
            value: If True then counts number of recommendations that are compliant.

        Returns:
            Count
        """
        return self._state.count(value)

    def urlencode(self, separator: str = "%20%20") -> str:
        """Encodes compliance into string which can be used in a URL.

        Args:
            separator:

        Returns:
            String that can be used in a URL
        """
        return separator.join([quote(symbol) for symbol in self.as_unicode()])
