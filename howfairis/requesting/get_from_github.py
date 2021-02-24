from .get_from_github_no_auth import get_from_github_no_auth
from .get_from_github_with_auth import get_from_github_with_auth


def get_from_github(url, url_type, apikeys=None):

    github_apikey_is_invalid = apikeys is not None and (apikeys.get("github-key") is None or
                                                        apikeys.get("github-user") is None)

    if apikeys is None or github_apikey_is_invalid:
        return get_from_github_no_auth(url, url_type)

    return get_from_github_with_auth(url, url_type, apikeys)
