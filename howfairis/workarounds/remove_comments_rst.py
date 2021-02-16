import warnings


def remove_comments_rst(text, fname):
    warnings.warn("Unable to ignore comments in RestructuredText format of {0}, checks will also see comments".format(fname))
    return text
