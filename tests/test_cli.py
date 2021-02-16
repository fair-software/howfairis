from click.testing import CliRunner
from howfairis.cli.cli import cli


runner = CliRunner()


def test_invalid_url():
    runner = CliRunner()
    response = runner.invoke(cli, [""])
    expected_message = "url should start with https://"
    assert response.exception.args[0] == expected_message


def test_url_not_git():
    runner = CliRunner()
    response = runner.invoke(cli, ["https://www.esciencecenter.nl"])
    expected_message = "Repository should be on github.com or on gitlab.com."
    assert response.exception.args[0] == expected_message


def test_url_not_repository():
    runner = CliRunner()
    response = runner.invoke(cli, ["https://github.com/fair-software"])
    expected_message = "url is not a repository"
    assert response.exception.args[0] == expected_message
