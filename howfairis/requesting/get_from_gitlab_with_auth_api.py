import requests


# https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits
def get_from_gitlab_with_auth_api(url, apikeys):

    headers = {"Authorization": "Bearer " + apikeys.get("gitlab")}
    return requests.get(url, headers)
