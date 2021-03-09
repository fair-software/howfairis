import re
from typing import Optional
from docutils.frontend import OptionParser
from docutils.nodes import GenericNodeVisitor
from docutils.nodes import Text
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from .compliance import Compliance
from .readme_format import ReadmeFormat


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

    def __init__(self, filename: Optional[str] = None, text: Optional[str] = None,
                 file_format: Optional[ReadmeFormat] = None, ignore_commented_badges: bool = True):

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
            self._remove_comments_rst()
        return self

    def _remove_comments_rst(self):
        """  """
        class CommentVisitor(GenericNodeVisitor):
            """ """

            def default_visit(self, node):
                if node.tagname == "comment":
                    return
                if isinstance(node, Text) and node.parent.tagname != "comment":
                    text.append(node.parent.rawsource)
                elif len(node.children) == 0:
                    text.append(node.rawsource)

            def default_departure(self, node):
                pass

        parser = Parser()
        settings = OptionParser(components=[Parser]).get_default_values()
        doc = new_document("", settings=settings)
        parser.parse(self.text, doc)

        # cobble together the rst text from all the leaf nodes
        visitor = CommentVisitor(doc)
        text = list()
        doc.walkabout(visitor)
        self.text = "\n\n".join([item for item in text if item != ""])
        return self

    def get_compliance(self) -> Optional[Compliance]:
        """Retrieve compliance from README based on presence of the FAIR Software badge.

        Returns:
            Compliance object when badge is found otherwise None.
        """

        if self.text is None:
            return None

        regex_string = \
            r"(?P<skip>^.*)" \
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
        regex = re.compile(regex_string, re.MULTILINE | re.DOTALL)
        matched = re.match(regex, self.text)

        if matched is None:
            return None

        groupdict = matched.groupdict()

        return Compliance(repository=groupdict.get("repository") == Readme.COMPLIANT_SYMBOL,
                          license_=groupdict.get("license") == Readme.COMPLIANT_SYMBOL,
                          registry=groupdict.get("registry") == Readme.COMPLIANT_SYMBOL,
                          citation=groupdict.get("citation") == Readme.COMPLIANT_SYMBOL,
                          checklist=groupdict.get("checklist") == Readme.COMPLIANT_SYMBOL)
