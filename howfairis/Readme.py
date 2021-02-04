import re
from typing import Optional

from docutils.core import publish_string
from docutils.nodes import SkipNode
from sphinx.application import Sphinx
from sphinx.builders.dummy import DummyBuilder
from sphinx.builders.text import TextBuilder
from sphinxcontrib.builders.rst import RstBuilder
from sphinxcontrib.writers.rst import RstWriter, RstTranslator

from .ReadmeFormat import ReadmeFormat


def _remove_comments_from_rst(rst):
    app = None
    return publish_string(source=rst, writer=RstWriter(DummyBuilder(app)))


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
