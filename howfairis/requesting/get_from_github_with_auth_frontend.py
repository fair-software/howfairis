import requests
from backoff import expo
from backoff import on_exception
from ratelimit import RateLimitException
from ratelimit import limits


# https://docs.github.com/en/rest/reference/rate-limit
@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=5000, period=3600)
def get_from_github_with_auth_frontend(url, apikeys):

    headers = {"Authorization": "Bearer " + apikeys.get("github")}
    return requests.get(url, headers)
