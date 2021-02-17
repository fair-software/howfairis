import re
from typing import Optional
from .compliance import Compliance
from .readme_format import ReadmeFormat
from .workarounds.remove_comments_rst import remove_comments_rst as remove_comments_with_workaround


class Readme:

    COMPLIANT_SYMBOL = "%E2%97%8F"
    NONCOMPLIANT_SYMBOL = "%E2%97%8B"
    SEPARATOR = "%20%20"

    def __init__(self, filename: Optional[str] = None, text: Optional[str] = None, file_format: Optional[str] = None,
                 ignore_commented_badges=True):

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
