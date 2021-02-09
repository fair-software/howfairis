from enum import Enum
from enum import auto
from enum import unique


@unique
class ReadmeFormat(Enum):
    """Format of a README document"""
    MARKDOWN = auto()
    RESTRUCTUREDTEXT = auto()
