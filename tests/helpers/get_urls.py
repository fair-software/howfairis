from howfairis.vcs_platform import Platform


def get_urls(vcs_platfrorm, owner, repo):
    if vcs_platfrorm == Platform.GITHUB:
        repo_url = "https://github.com/{0}/{1}".format(owner, repo)
        api_url = "https://api.github.com/repos/{0}/{1}".format(owner, repo)
        raw_url = "https://raw.githubusercontent.com/{0}/{1}".format(owner, repo)
        return repo_url, raw_url, api_url
