from enum import Enum
from enum import auto
from enum import unique


@unique
class ReadmeFormat(Enum):
    MARKDOWN = auto()
    RESTRUCTUREDTEXT = auto()
