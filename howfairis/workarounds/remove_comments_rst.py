from docutils.frontend import OptionParser
from docutils.parsers.rst import Parser
from docutils.utils import new_document


def remove_comments_rst(text):
    """  """

    parser = Parser()
    settings = OptionParser(components=[Parser]).get_default_values()
    doc = new_document("", settings=settings)
    parser.parse(text, doc)

    text = list()
    for child in doc.children:
        if child.tagname != "comment":
            text.append(child.rawsource)

    return "\n\n".join(text)
