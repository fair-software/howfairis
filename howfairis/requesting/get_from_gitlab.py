from howfairis.exceptions.howfairis_exception import HowfairisException
from .get_from_gitlab_api import get_from_gitlab_api
from .get_from_gitlab_frontend import get_from_gitlab_frontend
from .get_from_gitlab_raw import get_from_gitlab_raw


def get_from_gitlab(url, url_type, apikeys=None):

    if url_type == "api":
        return get_from_gitlab_api(url, apikeys)

    if url_type == "frontend":
        return get_from_gitlab_frontend(url, apikeys)

    if url_type == "raw":
        return get_from_gitlab_raw(url, apikeys)

    raise HowfairisException
