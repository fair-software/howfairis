from voluptuous import Any
from voluptuous import Optional
from voluptuous import Schema


schema = {
    Optional("skip_repository_checks_reason"): Any(str, None),
    Optional("skip_license_checks_reason"): Any(str, None),
    Optional("skip_registry_checks_reason"): Any(str, None),
    Optional("skip_citation_checks_reason"): Any(str, None),
    Optional("skip_checklist_checks_reason"): Any(str, None),
    Optional("ignore_commented_badges"): Any(bool, None)
}

validate_against_schema = Schema(schema)
