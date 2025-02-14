import requests


def get_from_external_no_auth_api(url):
    """ """
    return requests.get(url, timeout=15)
