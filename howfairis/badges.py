import re
from typing import Optional
from .compliance import Compliance
from .readme_format import ReadmeFormat


class Badges:
    """Container for the BADGES of a repository

    Args:
        text: A json blob containing the badges

    Attributes:
        text (str, None): json blob with all badges
    """

    COMPLIANT_SYMBOL = "%E2%97%8F"
    """this is a compliant symbol used in :py:func:`get_compliance`"""
    NONCOMPLIANT_SYMBOL = "%E2%97%8B"
    """this is a non-compliant symbol used in :py:func:`get_compliance`"""
    SEPARATOR = "%20%20"
    """this is a separator symbol used in :py:func:`get_compliance`"""

    def __init__(self, text: Optional[str] = None):

        self.text = text
        self.file_format = ReadmeFormat.NONE

    def __eq__(self, other):
        return \
            self.text == other.text

    def get_compliance(self) -> Optional[Compliance]:
        """Retrieve compliance from the list of badges based on presence of the FAIR Software badge.

        Returns:
            Compliance object when badge is found otherwise None.
        """

        if self.text is None:
            return None

        regex_string = \
            r"(?P<skip>^.*)" \
            "(?P<base>https://img.shields.io/badge/fair--software.eu)" \
            "-" \
            "(?P<repository>(" + Badges.COMPLIANT_SYMBOL + "|" + Badges.NONCOMPLIANT_SYMBOL + "))" \
            "(?:" + Badges.SEPARATOR + ")" \
            "(?P<license>(" + Badges.COMPLIANT_SYMBOL + "|" + Badges.NONCOMPLIANT_SYMBOL + "))" \
            "(?:" + Badges.SEPARATOR + ")" \
            "(?P<registry>(" + Badges.COMPLIANT_SYMBOL + "|" + Badges.NONCOMPLIANT_SYMBOL + "))" \
            "(?:" + Badges.SEPARATOR + ")" \
            "(?P<citation>(" + Badges.COMPLIANT_SYMBOL + "|" + Badges.NONCOMPLIANT_SYMBOL + "))" \
            "(?:" + Badges.SEPARATOR + ")" \
            "(?P<checklist>(" + Badges.COMPLIANT_SYMBOL + "|" + Badges.NONCOMPLIANT_SYMBOL + "))" \
            "-" \
            "(?P<color>red|orange|yellow|green)"
        regex = re.compile(regex_string, re.MULTILINE | re.DOTALL)
        matched = re.match(regex, self.text)

        if matched is None:
            return None

        groupdict = matched.groupdict()

        return Compliance(repository=groupdict.get("repository") == Badges.COMPLIANT_SYMBOL,
                          license_=groupdict.get("license") == Badges.COMPLIANT_SYMBOL,
                          registry=groupdict.get("registry") == Badges.COMPLIANT_SYMBOL,
                          citation=groupdict.get("citation") == Badges.COMPLIANT_SYMBOL,
                          checklist=groupdict.get("checklist") == Badges.COMPLIANT_SYMBOL)
