import pytest
from click.testing import CliRunner

from howfairis import __version__
from howfairis.cli import cli
from tests.contracts.cli import Contract


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
        expected = """## Uncomment a line if you want to skip a given category of checks

#skip_repository_checks_reason: <reason for skipping goes here>
#skip_license_checks_reason: <reason for skipping goes here>
#skip_registry_checks_reason: <reason for skipping goes here>
#skip_citation_checks_reason: <reason for skipping goes here>
#skip_checklist_checks_reason: <reason for skipping goes here>

include_comments: false

"""
        assert result.stdout == expected

    def test_version_option(self, invoke_cli):
        result = invoke_cli("--version")
        assert __version__ in result.stdout

    def test_with_an_url(self, invoke_cli):
        result = invoke_cli("https://github.com/fair-software/badge")
        expected = """Checking compliance with fair-software.eu...
url: https://github.com/fair-software/badge
(1/5) repository:
      ✓ has_open_repository
(2/5) license:
      ✓ has_license
(3/5) registry:
      × has_ascl_badge
      × has_bintray_badge
      × has_conda_badge
      × has_cran_badge
      × has_crates_badge
      × has_maven_badge
      × has_npm_badge
      × has_pypi_badge
      × has_rsd_badge
      ✓ is_on_github_marketplace
(4/5) citation:
      × has_citation_file
      ✓ has_citationcff_file
      × has_codemeta_file
      × has_zenodo_badge
      × has_zenodo_metadata_file
(5/5) checklist:
      × has_core_infrastructures_badge

Calculated compliance: ● ● ● ● ○

It seems you have not yet added the fair-software.eu badge to your README.md. You can do so by pasting the following snippet:

[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu)
"""
        assert result.exit_code == 1
        assert result.stdout == expected
