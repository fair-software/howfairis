from docutils.frontend import OptionParser
from docutils.nodes import GenericNodeVisitor
from docutils.nodes import Text
from docutils.parsers.rst import Parser
from docutils.utils import new_document


def remove_comments_rst(text):
    """  """

    class CommentVisitor(GenericNodeVisitor):
        """ """
        def default_visit(self, node):
            is_leaf = isinstance(node, Text)
            if node.tagname != "comment" and not is_leaf:
                text.append(node.rawsource)

        def default_departure(self, node):
            pass

    parser = Parser()
    settings = OptionParser(components=[Parser]).get_default_values()
    doc = new_document("", settings=settings)
    parser.parse(text, doc)
    visitor = CommentVisitor(doc)
    text = list()
    doc.walkabout(visitor)

    return "\n\n".join([item for item in text if item != ""])
