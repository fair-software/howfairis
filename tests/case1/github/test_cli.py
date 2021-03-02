import pytest
from click.testing import CliRunner
from howfairis import __version__
from howfairis.cli.cli import cli
from tests.contracts.cli import Contract
from tests.helpers import load_snippets_from_local_data
from tests.helpers import load_user_files_from_local_data


@pytest.fixture
def invoke_cli(mocker):
    runner = CliRunner()

    def _invoker(args):
        with mocker:
            return runner.invoke(cli, args, catch_exceptions=False)

    return _invoker


class TestCli(Contract):

    def test_show_default_config(self, invoke_cli):
        result = invoke_cli("--show-default-config")
        expected = load_user_files_from_local_data(__file__)["/.howfairis-default.yml"]
        assert result.stdout == expected

    def test_version_option(self, invoke_cli):
        result = invoke_cli("--version")
        assert __version__ in result.stdout

    def test_with_a_url(self, invoke_cli):
        result = invoke_cli("https://github.com/fair-software/repo1")
        expected = load_snippets_from_local_data(__file__)["/cli-no-args.txt"]
        assert result.exit_code == 1
        assert result.stdout == expected

    def test_with_nonexistent_path(self, invoke_cli):
        result = invoke_cli(["https://github.com/fair-software/repo1", "--path", "this/path/does-not-exist"])
        expected = load_snippets_from_local_data(__file__)["/cli-with-nonexistent-path.txt"]
        assert "Did not find a README[.md|.rst] file" in result.stdout, "Did not raise expected warning"
        assert "expect the compliance to suffer" in result.stdout, "Did not raise expected warning"
        assert result.exit_code == 1
        assert result.stdout == expected
