import sys
import click
from colorama import init as init_terminal_colors
from howfairis.__version__ import __version__
from howfairis.checker import DEFAULT_CONFIG_FILENAME
from howfairis.checker import Checker
from howfairis.cli.print_call_to_action import print_call_to_action
from howfairis.cli.print_default_config import print_default_config
from howfairis.cli.print_feedback_about_config_args import print_feedback_about_config_args
from howfairis.cli.print_feedback_about_repo_args import print_feedback_about_repo_args
from howfairis.cli.print_version import print_version
from howfairis.repo import Repo


# pylint: disable=too-many-arguments
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("-b", "--branch", default=None, type=click.STRING,
              help="Which git branch to use. Also accepts other git references like SHA or tag.")
@click.option("-u", "--user-config-filename", default=None, type=click.Path(),
              help="Name of the configuration file to control howfairis'es behavior. The configuration "
                   "file needs to be present on the local system and can include a relative path.")
@click.option("-d", "--show-default-config", default=False, is_flag=True,
              help="Show default configuration and exit.")
@click.option("-i", "--ignore-repo-config", default=False, is_flag=True,
              help="Ignore any configuration files on the remote.")
@click.option("-p", "--path", default=None, type=click.STRING,
              help="Relative path (on the remote). Use this if you want howfairis to look for a "
                   "README and a configuration file in a subdirectory.")
@click.option("-q", "--quiet", default=False, is_flag=True,
              help="Use this flag to disable all printing except errors.")
@click.option("-r", "--repo-config-filename", default=DEFAULT_CONFIG_FILENAME, type=click.STRING,
              help="Name of the configuration file to control howfairis'es behavior. The configuration "
                   "file needs to be on the remote, and takes into account the value of "
                   "--branch and --path. Default: .howfairis.yml")
@click.option("-t", "--show-trace", default=False, is_flag=True,
              help="Show full traceback on errors.")
@click.option("-v", "--version", default=False, is_flag=True,
              help="Show version and exit.")
@click.argument("url", required=False)
def cli(url=None, branch=None, user_config_filename=None, repo_config_filename=None, path=None,
        show_trace=False, version=False, ignore_repo_config=False, show_default_config=False, quiet=False):

    """Determine compliance with recommendations from fair-software.eu for the repository at URL. The following
    code repository platforms are supported:

    * https://github.com

    * https://gitlab.com (not including any self-hosted instances)
    """

    if show_trace is False:
        sys.tracebacklimit = 0

    if version is True:
        code = print_version(__version__, is_quiet=quiet)
        sys.exit(code)

    if show_default_config is True:
        code = print_default_config(is_quiet=quiet)
        sys.exit(code)

    print_feedback_about_repo_args(url, branch, path, is_quiet=quiet)
    print_feedback_about_config_args(ignore_repo_config, repo_config_filename, user_config_filename, is_quiet=quiet)

    init_terminal_colors()
    repo = Repo(url, branch, path)
    checker = Checker(repo, user_config_filename=user_config_filename, repo_config_filename=repo_config_filename,
                      ignore_repo_config=ignore_repo_config, is_quiet=quiet)

    previous_compliance = checker.readme.get_compliance()
    current_compliance = checker.check_five_recommendations()

    sys.exit(print_call_to_action(previous_compliance, current_compliance, checker, is_quiet=quiet))


if __name__ == "__main__":
    cli()
