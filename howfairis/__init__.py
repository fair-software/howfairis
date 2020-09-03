from howfairis.__version__ import __version__
from howfairis.check_badge import main as check_badge
from howfairis.check_checklist import main as check_checklist
from howfairis.check_citation import main as check_citation
from howfairis.check_license import main as check_license
from howfairis.check_registry import main as check_registry
from howfairis.check_repository import main as check_repository
from howfairis.howfairis import main as howfairis

__all__ = [
    "__version__",
    "check_badge",
    "check_checklist",
    "check_citation",
    "check_license",
    "check_registry",
    "check_repository",
    "howfairis"
]
