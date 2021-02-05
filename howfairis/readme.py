import re
from typing import Optional
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

        s = r"(?P<skip>^.*)" \
            "(?P<base>https://img.shields.io/badge/fair--software.eu)" \
            "-" \
            "(?P<repository>(%E2%97%8F|%E2%97%8B))" \
            "(?:%20%20)" \
            "(?P<license>(%E2%97%8F|%E2%97%8B))" \
            "(?:%20%20)" \
            "(?P<registry>(%E2%97%8F|%E2%97%8B))" \
            "(?:%20%20)" \
            "(?P<citation>(%E2%97%8F|%E2%97%8B))" \
            "(?:%20%20)" \
            "(?P<checklist>(%E2%97%8F|%E2%97%8B))" \
            "-" \
            "(?P<color>red|orange|yellow|green)"
        regex = re.compile(s, re.MULTILINE|re.DOTALL)
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
