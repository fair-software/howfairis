from .__version__ import __version__
from .checker import Checker
from .compliance import Compliance
from .config import Config
from .repo import Repo
from .code_repository_platforms import Platform


__author__ = "https://github.com/jspaaks"
__email__ = 'j.spaaks@esciencecenter.nl'

__all__ = [
    "__version__",
    "Checker",
    "Compliance",
    "Config",
    "Platform",
    "Repo"
]
