from urllib.parse import urlparse
from howfairis.code_repository_platforms import Platform


def get_urls(code_repository_platform, owner, repo):

    repo_url = None
    api_url = None
    raw_url = None

    if code_repository_platform == Platform.GITHUB:
        repo_url = "https://github.com/{0}/{1}".format(owner, repo)
        api_url = "https://api.github.com/repos/{0}/{1}".format(owner, repo)
        raw_url = "https://raw.githubusercontent.com/{0}/{1}".format(owner, repo)

    if code_repository_platform == Platform.GITLAB:
        repo_url = "https://gitlab.com/{0}/{1}".format(owner, repo)
        api_url = "https://gitlab.com/api/v4/projects/{0}%2F{1}".format(owner, repo)
        raw_url = "https://gitlab.com/{0}/{1}/-/raw".format(owner, repo)

    parsed_url = urlparse(repo_url)
    reuse_url = (
        f"https://api.reuse.software/status/{parsed_url.netloc}{parsed_url.path}.json"
    )

    return repo_url, raw_url, api_url, reuse_url
