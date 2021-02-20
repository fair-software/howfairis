import requests


def get_from_gitlab_with_auth_frontend(url, apikeys):

    headers = {"Authorization": "Bearer " + apikeys.get("gitlab")}
    return requests.get(url, headers)
