from backoff import expo
from backoff import on_exception
from ratelimit import RateLimitException
from ratelimit import limits
from .get_from_github_with_auth_api import get_from_github_with_auth_api
from .get_from_github_with_auth_frontend import get_from_github_with_auth_frontend
from .get_from_github_with_auth_raw import get_from_github_with_auth_raw


# https://docs.github.com/en/rest/reference/rate-limit
@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=5000, period=3600)
def get_from_github_with_auth(url, url_type, apikeys):

    if url_type == "api":
        return get_from_github_with_auth_api(url, apikeys)

    if url_type == "frontend":
        return get_from_github_with_auth_frontend(url, apikeys)

    if url_type == "raw":
        return get_from_github_with_auth_raw(url, apikeys)

    raise NotImplementedError
