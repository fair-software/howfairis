from howfairis.cli import github_readme_creation_check
from howfairis.vcs_platform import Platform


def test_github_readme_creation_check_platform():
    actual_return_code = github_readme_creation_check("", "", Platform.GITLAB, None)
    expected_return_code = 0
    assert actual_return_code == expected_return_code
