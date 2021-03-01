import requests


def get_from_gitlab_no_auth_raw(url):
    return requests.get(url)
