import re
from typing import Optional
from howfairis.compliance import Compliance


class Readme:

    COMPLIANT_SYMBOL = "%E2%97%8F"
    NONCOMPLIANT_SYMBOL = "%E2%97%8B"
    SEPARATOR = "%20%20"

    def __init__(self, filename: Optional[str] = None, text: Optional[str] = None, fmt: Optional[str] = None):
        self.filename = filename
        self.text = text
        self.fmt = fmt

    def __eq__(self, other):
        return \
            self.filename == other.filename and \
            self.text == other.text and \
            self.fmt == other.fmt

    def get_compliance(self):

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
