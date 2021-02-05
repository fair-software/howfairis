from enum import Enum
from enum import auto
from enum import unique


@unique
class Platform(Enum):
    BITBUCKET = auto()
    GITHUB = auto()
    GITLAB = auto()
