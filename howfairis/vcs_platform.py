from enum import Enum
from enum import auto
from enum import unique


@unique
class Platform(Enum):
    """Type of version control system platform"""
    GITHUB = auto()
    GITLAB = auto()
