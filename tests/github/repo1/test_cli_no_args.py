import pytest
from click.testing import CliRunner
from howfairis import __version__
from howfairis.cli.cli import cli
from tests.contracts.cli import Contract
from tests.helpers import load_files_from_local_data


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
        expected = load_files_from_local_data(__file__, "user")['/howfairis.default.yml']
        assert result.stdout == expected

    def test_version_option(self, invoke_cli):
        result = invoke_cli("--version")
        assert __version__ in result.stdout

    def test_with_a_url(self, invoke_cli):
        result = invoke_cli("https://github.com/fair-software/badge")
        expected = load_files_from_local_data(__file__, "output")['/cli_no_args.txt']
        assert result.exit_code == 1
        assert result.stdout == expected
