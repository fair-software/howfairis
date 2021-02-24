import requests


def get_from_github_with_auth_api(url, apikeys):

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    username = apikeys.get("github-user")
    key = apikeys.get("github-key")

    return requests.get(url, headers, auth=(username, key))
