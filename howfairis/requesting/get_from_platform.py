from howfairis.code_repository_platforms import Platform
from howfairis.exceptions.howfairis_unknown_platform_exception import HowfairisUnknownPlatformException
from .get_from_github import get_from_github
from .get_from_gitlab import get_from_gitlab


def get_from_platform(platform: Platform, url: str, url_type: str, apikeys=None):

    if platform == Platform.GITHUB:
        return get_from_github(url, url_type, apikeys)

    if platform == Platform.GITLAB:
        return get_from_gitlab(url, url_type, apikeys)

    raise HowfairisUnknownPlatformException
