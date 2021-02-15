from click.testing import CliRunner
from howfairis import cli


def test_valid_url():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["https://github.com/fair-software/howfairis"])
    expected_exit_code = str(0)
    actual_exit_code = str(result.exit_code)
    assert actual_exit_code == expected_exit_code


def test_invalid_url():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["howfairis"])
    expected_exception = "url should start with https://"
    assert str(result.exception) == expected_exception


def test_no_github():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["https://www.esciencecenter.nl"])
    expected_exception = "Repository should be on github.com or on gitlab.com."
    assert str(result.exception) == expected_exception


def test_no_repository():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["https://github.com/fair-software"])
    expected_exception = "url is not a repository"
    assert str(result.exception) == expected_exception
