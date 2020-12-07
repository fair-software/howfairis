from voluptuous import Any
from voluptuous import Optional
from voluptuous import Schema


schema = {
    Optional("force_repository"): Any(bool, None),
    Optional("force_license"): Any(bool, None),
    Optional("force_registry"): Any(bool, None),
    Optional("force_citation"): Any(bool, None),
    Optional("force_checklist"): Any(bool, None),
    Optional("include_comments"): Any(bool, None)
}

validate_against_schema = Schema(schema)
