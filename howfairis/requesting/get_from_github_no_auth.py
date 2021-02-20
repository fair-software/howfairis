from backoff import expo
from backoff import on_exception
from ratelimit import RateLimitException
from ratelimit import limits
from .get_from_github_no_auth_api import get_from_github_no_auth_api
from .get_from_github_no_auth_frontend import get_from_github_no_auth_frontend
from .get_from_github_no_auth_raw import get_from_github_no_auth_raw


# https://docs.github.com/en/rest/reference/rate-limit
@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=60, period=3600)
def get_from_github_no_auth(url, url_type):

    if url_type == "api":
        return get_from_github_no_auth_api(url)

    if url_type == "frontend":
        return get_from_github_no_auth_frontend(url)

    if url_type == "raw":
        return get_from_github_no_auth_raw(url)

    raise NotImplementedError
