from howfairis.exceptions.howfairis_exception import HowfairisException
from .get_from_github_api import get_from_github_api
from .get_from_github_frontend import get_from_github_frontend
from .get_from_github_raw import get_from_github_raw


def get_from_github(url, url_type, apikeys=None):

    if url_type == "api":
        return get_from_github_api(url, apikeys)

    if url_type == "frontend":
        return get_from_github_frontend(url, apikeys)

    if url_type == "raw":
        return get_from_github_raw(url, apikeys)

    raise HowfairisException
