import requests


def get_from_github_with_auth_frontend(url, apikeys):

    headers = {
        "Accept": "text/javascript, text/html, application/xml"
    }

    username = apikeys.get("github-user")
    key = apikeys.get("github-key")

    return requests.get(url, headers, auth=(username, key))
