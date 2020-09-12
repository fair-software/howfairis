from enum import Enum, unique, auto


@unique
class Platform(Enum):
    GITHUB = auto()
    GITLAB = auto()
