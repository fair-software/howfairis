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
            if isinstance(node, Text):
                text.append(node.parent.rawsource)
            elif len(node.children) == 0:
                text.append(node.rawsource)

        def default_departure(self, node):
            pass

    parser = Parser()
    settings = OptionParser(components=[Parser]).get_default_values()
    doc = new_document("", settings=settings)
    parser.parse(text, doc)

    # remove nodes that are comments
    doc.children = [child for child in doc.children if child.tagname != "comment"]

    # cobble together the rst text from all the leaf nodes
    visitor = CommentVisitor(doc)
    text = list()
    doc.walkabout(visitor)

    return "\n\n".join([item for item in text if item != ""])
