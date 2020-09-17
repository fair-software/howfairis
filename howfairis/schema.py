from voluptuous import Any
from voluptuous import Optional
from voluptuous import Schema


schema = {
    Optional("force"): Any({
        Optional("repository"): Any(bool, None),
        Optional("license"): Any(bool, None),
        Optional("registry"): Any(bool, None),
        Optional("citation"): Any(bool, None),
        Optional("checklist"): Any(bool, None),
    }, None),
    Optional("include_comments"): Any(bool, None)
}

validate_against_schema = Schema(schema)
