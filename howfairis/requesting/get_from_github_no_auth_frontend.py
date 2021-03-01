import requests


def get_from_github_no_auth_frontend(url):
    return requests.get(url)
