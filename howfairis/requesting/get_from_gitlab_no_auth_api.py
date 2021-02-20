import requests


def get_from_gitlab_no_auth_api(url):
    return requests.get(url)
