import requests


# https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits
def get_from_gitlab_with_auth_raw(url, apikeys):

    headers = {}

    username = apikeys.get("gitlab").get("username")
    key = apikeys.get("gitlab").get("key")

    return requests.get(url, headers, auth=(username, key))
