import requests


def get_from_gitlab_no_auth_frontend(url):
    return requests.get(url)
