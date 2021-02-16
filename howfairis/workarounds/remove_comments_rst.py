import warnings


def remove_comments_rst(text, fname):
    warnings.warn("Using workaround to remove comments from {0}.".format(fname))
    return text
