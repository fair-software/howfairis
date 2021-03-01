import sys
from backoff import expo
from backoff import on_exception
from ratelimit import RateLimitException
from ratelimit import limits
from .get_from_gitlab_no_auth_api import get_from_gitlab_no_auth_api
from .get_from_gitlab_no_auth_frontend import get_from_gitlab_no_auth_frontend
from .get_from_gitlab_no_auth_raw import get_from_gitlab_no_auth_raw


def get_calls():

    if "pytest" in sys.modules:
        # in testing, the api is mocked, so we overrule the rate limit
        return 1e6
    # normal operation, 60 calls per hour for unauthenticated github api access
    return 500


# https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits
@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=get_calls(), period=60)
def get_from_gitlab_no_auth(url, url_type):

    if url_type == "api":
        return get_from_gitlab_no_auth_api(url)

    if url_type == "frontend":
        return get_from_gitlab_no_auth_frontend(url)

    if url_type == "raw":
        return get_from_gitlab_no_auth_raw(url)

    raise NotImplementedError
