import re
from typing import Optional
from howfairis.compliance import Compliance
from howfairis.readme_format import ReadmeFormat


class Readme:
    """Container for the README of a repository

    Attributes:
        filename (str): Name of README
        text (str): Content of README
        fmt (ReadmeFormat): Format of README

    """
    def __init__(self, filename: Optional[str], text: Optional[str], fmt: Optional[ReadmeFormat]):
        self.filename = filename
        self.text = text
        self.fmt = fmt

    def __eq__(self, other):
        return \
            self.filename == other.filename and \
            self.text == other.text and \
            self.fmt == other.fmt

    def get_compliance(self, compliant: str = "%E2%97%8F", noncompliant: str = "%E2%97%8B",
                       separator: str = "%20%20") -> Optional[Compliance]:
        """Retrieve compliance from README based on presence of the FAIR Software badge.

        Args:
            compliant: Symbol used in badge url for compliant
            noncompliant: Symbol used in badge url for non-compliant
            separator: Symbol used in badge url for separating recommendations

        Returns:
            Compliance object when badge is found otherwise None.
        """

        s = r"(?P<skip>^.*)" \
            "(?P<base>https://img.shields.io/badge/fair--software.eu)" \
            "-" \
            "(?P<repository>(" + compliant + "|" + noncompliant + "))" \
            "(?:" + separator + ")" \
            "(?P<license>(" + compliant + "|" + noncompliant + "))" \
            "(?:" + separator + ")" \
            "(?P<registry>(" + compliant + "|" + noncompliant + "))" \
            "(?:" + separator + ")" \
            "(?P<citation>(" + compliant + "|" + noncompliant + "))" \
            "(?:" + separator + ")" \
            "(?P<checklist>(" + compliant + "|" + noncompliant + "))" \
            "-" \
            "(?P<color>red|orange|yellow|green)"
        regex = re.compile(s, re.MULTILINE | re.DOTALL)
        matched = re.match(regex, self.text)

        if matched is None:
            return None

        groupdict = matched.groupdict()

        return Compliance(repository=groupdict.get("repository") == compliant,
                          license_=groupdict.get("license") == compliant,
                          registry=groupdict.get("registry") == compliant,
                          citation=groupdict.get("citation") == compliant,
                          checklist=groupdict.get("checklist") == compliant,
                          compliant_symbol=compliant,
                          noncompliant_symbol=noncompliant)
