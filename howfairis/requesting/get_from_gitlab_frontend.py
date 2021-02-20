from .get_from_gitlab_frontend_no_auth import get_from_gitlab_frontend_no_auth
from .get_from_gitlab_frontend_with_auth import get_from_gitlab_frontend_with_auth


def get_from_gitlab_frontend(url, apikeys=None):

    if apikeys is None:
        return get_from_gitlab_frontend_no_auth(url)

    return get_from_gitlab_frontend_with_auth(url, apikeys)
