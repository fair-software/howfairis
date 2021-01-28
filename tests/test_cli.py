import pytest
from click.testing import CliRunner, Result
from howfairis import cli


def test_invalid_url():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["howfairis"])
    expected_exception = "url should start with https://"
    assert str(result.exception) == expected_exception

def test_no_github():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["https://www.esciencecenter.nl"])
    expected_exception = "Repository should be on github.com or on gitlab.com"
    assert str(result.exception) == expected_exception

def test_no_repository():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["https://github.com/fair-software"])
    expected_exception = "url is not a repository"
    assert str(result.exception) == expected_exception

