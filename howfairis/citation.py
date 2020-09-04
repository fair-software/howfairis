import re


def has_zenodo_badge(s):
    regex = r"!\[.*\]\(https://zenodo\.org/badge/DOI/10\.5281/zenodo" + \
            r"\.[0-9]*\.svg\)\]\(https://doi\.org/10\.5281/zenodo\.[0-9]*\)"
    return re.compile(regex).search(s) is not None
