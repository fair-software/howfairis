from . import mixins
from .__version__ import __version__
from .HowFairIsChecker import HowFairIsChecker
from .Platform import Platform
from .schema import validate_against_schema


__author__ = "https://github.com/jspaaks"
__email__ = 'j.spaaks@esciencecenter.nl'

__all__ = [
    "__version__",
    "HowFairIsChecker",
    "mixins",
    "Platform",
    "validate_against_schema"
]
