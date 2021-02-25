import os


def get_apikeys_from_env_vars():
    apikey_github = os.getenv("APIKEY_GITHUB", None)
    apikey_gitlab = os.getenv("APIKEY_GITLAB", None)

    if apikey_github is None:
        github_user, github_key = None, None
    else:
        github_user, github_key = apikey_github.split(":")

    if apikey_gitlab is None:
        gitlab_user, gitlab_key = None, None
    else:
        gitlab_user, gitlab_key = apikey_github.split(":")

    return {
        "github-key": github_key,
        "github-user": github_user,
        "gitlab-key": gitlab_key,
        "gitlab-user": gitlab_user
    }
