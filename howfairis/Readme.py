from typing import Optional

from docutils.core import publish_string
from docutils.nodes import SkipNode
from docutils.writers.html5_polyglot import Writer, HTMLTranslator

from .ReadmeFormat import ReadmeFormat


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

    def to_html(self, remove_comments=False):
        class CommentIgnorer(HTMLTranslator):
            def visit_comment(self, node):
                raise SkipNode

        class CommentlessHtmlWriter(Writer):
            def __init__(self):
                super().__init__()
                self.translator_class = CommentIgnorer

        if self.fmt == ReadmeFormat.RESTRUCTUREDTEXT:
            if remove_comments:
                return publish_string(source=self.text, writer=CommentlessHtmlWriter())
            return publish_string(source=self.text, writer=Writer())
