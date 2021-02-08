import re
from typing import Optional
from docutils.nodes import GenericNodeVisitor
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from .readme_format import ReadmeFormat


def _remove_comments_from_rst(rst):
    parser = Parser()
    doc = new_document("")
    parser.parse(rst, doc)
    commented_lines = set()

    class CommentLineVisitor(GenericNodeVisitor):
        def default_visit(self, node):
            pass

        def default_departure(self, node):
            pass

        def visit_comment(self, node):
            commented_lines.add(node.line - 1)

    visitor = CommentLineVisitor(doc)
    doc.walkabout(visitor)

    if not commented_lines:
        # No comments found, return as is
        return rst
    # Remove text without the lines which are comments
    return ''.join([l for i, l in enumerate(rst.splitlines(keepends=True)) if i not in commented_lines])


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
