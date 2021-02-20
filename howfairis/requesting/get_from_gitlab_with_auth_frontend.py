import requests


def get_from_gitlab_with_auth_frontend(url, apikeys):

    headers = {
        "Accept": "text/javascript, text/html, application/xml"
    }

    username = apikeys.get("gitlab").get("username")
    key = apikeys.get("gitlab").get("key")

    return requests.get(url, headers, auth=(username, key))
