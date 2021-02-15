import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        if "github" in item.nodeid:
            item.add_marker(pytest.mark.github)
        if "gitlab" in item.nodeid:
            item.add_marker(pytest.mark.gitlab)
        if item.nodeid.split("::")[1].startswith("TestRepo"):
            item.add_marker(pytest.mark.repo)
        if item.nodeid.split("::")[1].startswith("TestChecker"):
            item.add_marker(pytest.mark.checker)
        if item.nodeid.split("::")[1].startswith("TestCompliance"):
            item.add_marker(pytest.mark.compliance)
