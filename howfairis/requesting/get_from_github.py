from .get_from_github_no_auth import get_from_github_no_auth
from .get_from_github_with_auth import get_from_github_with_auth


def get_from_github(url, url_type, apikeys=None):

    if apikeys and apikeys.get("github-key") and apikeys.get("github-user"):
        return get_from_github_with_auth(url, url_type, apikeys)

    return get_from_github_no_auth(url, url_type)
