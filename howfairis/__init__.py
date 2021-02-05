from .__version__ import __version__
from .compliance import Compliance
from .repo import Repo
from .config import Config
from .checker import Checker


__author__ = "https://github.com/jspaaks"
__email__ = 'j.spaaks@esciencecenter.nl'

__all__ = [
    "__version__",
    "Checker",
    "Compliance",
    "Config",
    "Repo"
]
