from .howfairis_exception import HowfairisException


class HowfairisUnknownPlatformException(HowfairisException):
    """Raised when trying to use an unsupported code repository platform."""
