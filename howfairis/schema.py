from voluptuous import Optional
from voluptuous import Schema


schema = {
    Optional("force"): {
        Optional("repository"): bool,
        Optional("license"): bool,
        Optional("registry"): bool,
        Optional("citation"): bool,
        Optional("checklist"): bool,
    }
}

validate_against_schema = Schema(schema)
