from .get_from_gitlab_with_auth_api import get_from_gitlab_with_auth_api
from .get_from_gitlab_with_auth_frontend import get_from_gitlab_with_auth_frontend
from .get_from_gitlab_with_auth_raw import get_from_gitlab_with_auth_raw


def get_from_gitlab_with_auth(url, url_type, apikeys):

    if url_type == "api":
        return get_from_gitlab_with_auth_api(url, apikeys)

    if url_type == "frontend":
        return get_from_gitlab_with_auth_frontend(url, apikeys)

    if url_type == "raw":
        return get_from_gitlab_with_auth_raw(url, apikeys)

    raise NotImplementedError
