from .__version__ import __version__
from .check_badge import main as check_badge
from .check_checklist import main as check_checklist
from .check_citation import main as check_citation
from .check_license import main as check_license
from .check_registry import main as check_registry
from .check_repository import main as check_repository
from .howfairis import main as howfairis

__all__ = [
    "__version__",
    "check_badge",
    "check_checklist",
    "check_citation",
    "check_license",
    "check_registry",
    "check_repository"
]
