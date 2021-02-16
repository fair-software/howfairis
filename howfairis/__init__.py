from . import exceptions
from . import workarounds
from .__version__ import __version__
from .checker import Checker
from .code_repository_platforms import Platform
from .compliance import Compliance
from .repo import Repo


__author__ = "https://github.com/jspaaks"
__email__ = 'j.spaaks@esciencecenter.nl'

__all__ = [
    "exceptions",
    "__version__",
    "Checker",
    "Compliance",
    "Platform",
    "Repo",
    "workarounds"
]
