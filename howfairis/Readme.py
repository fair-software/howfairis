import re
from functools import lru_cache
from typing import Optional

from docutils.frontend import OptionParser
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from rstfmt.rst_extras import register
from rstfmt.rstfmt import format_node, Formatters

from .ReadmeFormat import ReadmeFormat

_register_completed = False


@lru_cache(maxsize=None)
def _register_docutils():
    register()


def _remove_comments_from_rst(rst):
    _register_docutils()
    parser = Parser()
    settings = OptionParser(
        components=[Parser]
    ).get_default_values()
    doc = new_document("", settings=settings)
    parser.parse(rst, doc)

    # Formatter of rstfmt retains comment, temporary disable that
    orig_comment = Formatters.comment

    def comment(_node, _ctx):
        return []

    Formatters.comment = comment

    commentless_rst = format_node(None, doc)

    Formatters.comment = orig_comment
    return commentless_rst


def _remove_comments_from_md(md):
    return re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)


class Readme:
    def __init__(self, filename: Optional[str] = None, text: Optional[str] = None, fmt: Optional[ReadmeFormat] = None):
        self.filename = filename
        self.text = text
        self.fmt = fmt

    def __eq__(self, other):
        return \
            self.filename == other.filename and \
            self.text == other.text and \
            self.fmt == other.fmt

    def remove_comments(self):
        if self.fmt == ReadmeFormat.MARKDOWN:
            self.text = _remove_comments_from_md(self.text)
        elif self.fmt == ReadmeFormat.RESTRUCTUREDTEXT:
            self.text = _remove_comments_from_rst(self.text)
        else:
            raise Exception('Unable remove comments unknown format for Readme')
