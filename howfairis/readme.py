import re
from typing import Optional
from .compliance import Compliance
from .readme_format import ReadmeFormat
from .workarounds.remove_comments_rst import remove_comments_rst as remove_comments_with_workaround


class Readme:
    """Container for the README of a repository

    Args:
        filename: Name of README
        text: Content of README
        file_format: Format of README. It is used to ignore commented out badges.
        ignore_commented_badges: If False commented out badges will be considered.

    Attributes:
        filename (str, None): Name of README
        text (str, None): Content of README
        file_format (ReadmeFormat, None): Format of README
    """

    COMPLIANT_SYMBOL = "%E2%97%8F"
    """this is a compliant symbol used in :py:func:`get_compliance`"""
    NONCOMPLIANT_SYMBOL = "%E2%97%8B"
    """this is a non-compliant symbol used in :py:func:`get_compliance`"""
    SEPARATOR = "%20%20"
    """this is a separator symbol used in :py:func:`get_compliance`"""

    def __init__(self, filename: Optional[str] = None, text: Optional[str] = None, file_format: Optional[ReadmeFormat] = None,
                 ignore_commented_badges: bool = True):

        self.filename = filename
        self.text = text
        self.file_format = file_format

        if ignore_commented_badges is True:
            self._remove_comments()

    def __eq__(self, other):
        return \
            self.filename == other.filename and \
            self.text == other.text and \
            self.file_format == other.file_format

    def _remove_comments(self):
        if self.file_format == ReadmeFormat.MARKDOWN:
            self.text = re.sub(r"<!--.*?-->", "", self.text, flags=re.DOTALL)
        if self.file_format == ReadmeFormat.RESTRUCTUREDTEXT:
            self.text = remove_comments_with_workaround(self.text, self.filename)
        return self

    def get_compliance(self) -> Optional[Compliance]:
        """Retrieve compliance from README based on presence of the FAIR Software badge.

        Returns:
            Compliance object when badge is found otherwise None.
        """

        if self.text is None:
            return None

        s = r"(?P<skip>^.*)" \
            "(?P<base>https://img.shields.io/badge/fair--software.eu)" \
            "-" \
            "(?P<repository>(" + Readme.COMPLIANT_SYMBOL + "|" + Readme.NONCOMPLIANT_SYMBOL + "))" \
            "(?:" + Readme.SEPARATOR + ")" \
            "(?P<license>(" + Readme.COMPLIANT_SYMBOL + "|" + Readme.NONCOMPLIANT_SYMBOL + "))" \
            "(?:" + Readme.SEPARATOR + ")" \
            "(?P<registry>(" + Readme.COMPLIANT_SYMBOL + "|" + Readme.NONCOMPLIANT_SYMBOL + "))" \
            "(?:" + Readme.SEPARATOR + ")" \
            "(?P<citation>(" + Readme.COMPLIANT_SYMBOL + "|" + Readme.NONCOMPLIANT_SYMBOL + "))" \
            "(?:" + Readme.SEPARATOR + ")" \
            "(?P<checklist>(" + Readme.COMPLIANT_SYMBOL + "|" + Readme.NONCOMPLIANT_SYMBOL + "))" \
            "-" \
            "(?P<color>red|orange|yellow|green)"
        regex = re.compile(s, re.MULTILINE | re.DOTALL)
        matched = re.match(regex, self.text)

        if matched is None:
            return None

        groupdict = matched.groupdict()

        return Compliance(repository=groupdict.get("repository") == Readme.COMPLIANT_SYMBOL,
                          license_=groupdict.get("license") == Readme.COMPLIANT_SYMBOL,
                          registry=groupdict.get("registry") == Readme.COMPLIANT_SYMBOL,
                          citation=groupdict.get("citation") == Readme.COMPLIANT_SYMBOL,
                          checklist=groupdict.get("checklist") == Readme.COMPLIANT_SYMBOL)
