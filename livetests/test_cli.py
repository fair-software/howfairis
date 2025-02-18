import os

from click.testing import CliRunner
from howfairis.cli.cli import cli


def test_valid_github_url_unauthenticated():
    assert os.getenv("APIKEY_GITHUB") is None, "This test should run unauthenticated"
    runner = CliRunner()
    result = runner.invoke(cli, ["https://github.com/fair-software/howfairis"])
    expected_exit_code = str(0)
    actual_exit_code = str(result.exit_code)
    assert actual_exit_code == expected_exit_code


def test_valid_gitlab_url_unauthenticated():
    assert os.getenv("APIKEY_GITLAB") is None, "This test should run unauthenticated"
    runner = CliRunner()
    result = runner.invoke(cli, ["https://gitlab.com/jspaaks/howfairis-livetest"])
    expected_exit_code = str(0)
    actual_exit_code = str(result.exit_code)
    assert actual_exit_code == expected_exit_code


def test_invalid_url():
    runner = CliRunner()
    result = runner.invoke(cli, ["howfairis"])
    expected_exception = "url should start with https://"
    assert str(result.exception) == expected_exception


def test_no_github():
    runner = CliRunner()
    result = runner.invoke(cli, ["https://www.esciencecenter.nl"])
    expected_exception = "Repository should be on github.com or on gitlab.com."
    assert str(result.exception) == expected_exception


def test_no_repository():
    runner = CliRunner()
    result = runner.invoke(cli, ["https://github.com/fair-software"])
    expected_exception = "url is not a repository"
    assert str(result.exception) == expected_exception


def test_cli_shows_warning_for_nonexistent_path():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "https://github.com/fair-software/howfairis",
            "--path",
            "this/path/does-not-exist",
        ],
    )
    assert (
        "Proceeding without it -- expect the compliance to suffer" in result.stdout
    ), "Did not raise expected warning"
    assert result.exit_code == 1
