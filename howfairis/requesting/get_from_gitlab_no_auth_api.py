import requests


def get_from_gitlab_no_auth_api(url):

    headers = {
        "Accept": "application/json"
    }

    return requests.get(url, headers)
