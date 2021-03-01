import requests


def get_from_github_no_auth_api(url):
    return requests.get(url)
