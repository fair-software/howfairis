from howfairis.vcs_platform import Platform


def get_urls(vcs_platform, owner, repo):

    repo_url = None
    api_url = None
    raw_url = None

    if vcs_platform == Platform.GITHUB:
        repo_url = "https://github.com/{0}/{1}".format(owner, repo)
        api_url = "https://api.github.com/repos/{0}/{1}".format(owner, repo)
        raw_url = "https://raw.githubusercontent.com/{0}/{1}".format(owner, repo)

    if vcs_platform == Platform.GITLAB:
        repo_url = "https://gitlab.com/{0}/{1}".format(owner, repo)
        api_url = "https://gitlab.com/api/v4/projects/{0}%2F{1}".format(owner, repo)
        raw_url = "https://gitlab.com/{0}/{1}/-/raw".format(owner, repo)

    return repo_url, raw_url, api_url
