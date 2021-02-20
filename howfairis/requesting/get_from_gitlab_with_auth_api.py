import requests


# https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits
def get_from_gitlab_with_auth_api(url, apikeys):

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    username = apikeys.get("gitlab").get("username")
    key = apikeys.get("gitlab").get("key")

    return requests.get(url, headers, auth=(username, key))
