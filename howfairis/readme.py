from typing import Optional
import re
from howfairis.compliance import Compliance


class Readme:
    def __init__(self, filename: Optional[str] = None, text: Optional[str] = None, fmt: Optional[str] = None):
        self.filename = filename
        self.text = text
        self.fmt = fmt

    def __eq__(self, other):
        return \
            self.filename == other.filename and \
            self.text == other.text and \
            self.fmt == other.fmt

    def get_compliance(self, compliant="%E2%97%8F", noncompliant="%E2%97%8B", separator="%20%20"):

        regex = r"(?P<skip>.*)" \
                "(?P<base>https://img.shields.io/badge/fair--software.eu)" + \
                "-" + \
                "(?P<repository>(" + compliant + "|" + noncompliant + "))" + \
                "(?:" + separator + ")" + \
                "(?P<license>(" + compliant + "|" + noncompliant + "))" + \
                "(?:" + separator + ")" + \
                "(?P<registry>(" + compliant + "|" + noncompliant + "))" + \
                "(?:" + separator + ")" + \
                "(?P<citation>(" + compliant + "|" + noncompliant + "))" + \
                "(?:" + separator + ")" + \
                "(?P<checklist>(" + compliant + "|" + noncompliant + "))" + \
                "-" + \
                "(?P<color>red|orange|yellow|green)"

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
