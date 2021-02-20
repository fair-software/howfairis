import requests


# https://docs.github.com/en/rest/reference/rate-limit
def get_from_github_frontend_no_auth(url):
    return requests.get(url)
