from .get_from_gitlab_no_auth import get_from_gitlab_no_auth
from .get_from_gitlab_with_auth import get_from_gitlab_with_auth


def get_from_gitlab(url, url_type, apikeys=None):

    if apikeys is None:
        return get_from_gitlab_no_auth(url, url_type)

    return get_from_gitlab_with_auth(url, url_type, apikeys)
