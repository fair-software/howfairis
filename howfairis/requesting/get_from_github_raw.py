from .get_from_github_raw_no_auth import get_from_github_raw_no_auth
from .get_from_github_raw_with_auth import get_from_github_raw_with_auth


def get_from_github_raw(url, apikeys=None):

    if apikeys is None:
        return get_from_github_raw_no_auth(url)

    return get_from_github_raw_with_auth(url, apikeys)
