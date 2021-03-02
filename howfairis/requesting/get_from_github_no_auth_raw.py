import requests


def get_from_github_no_auth_raw(url):
    return requests.get(url)
