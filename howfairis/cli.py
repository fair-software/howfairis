import os
import sys
import click
from colorama import init as init_terminal_colors
from howfairis.__version__ import __version__
from howfairis.checker import Checker
from howfairis.repo import Repo


def _exit_with_call_to_action(previous_compliance, current_compliance, readme, is_quiet=False):

    badge = current_compliance.calc_badge(readme.file_format)

    if not is_quiet:
        print("\nCalculated compliance: " + " ".join(current_compliance.as_unicode()) + "\n")

    if previous_compliance is None:
        if not is_quiet:
            print("It seems you have not yet added the fair-software.eu badge to " +
                  "your {0}. You can do so by pasting the following snippet:\n\n{1}"
                  .format(readme.filename, badge))
        sys.exit(1)

    if current_compliance == previous_compliance:
        if not is_quiet:
            print("Expected badge is equal to the actual badge. It's all good.\n")
        sys.exit(0)

    if current_compliance.count() > previous_compliance.count():
        if not is_quiet:
            print("Congratulations! The compliance of your repository exceeds " +
                  "the current fair-software.eu badge in your " +
                  "{0}. You can replace it with the following snippet:\n\n{1}"
                  .format(readme.filename, badge))
        sys.exit(1)

    if not is_quiet:
        print("The compliance of your repository is different from the current " +
              "fair-software.eu badge in your " +
              "{0}. Please replace it with the following snippet:\n\n{1}"
              .format(readme.filename, badge))

    sys.exit(1)


def _exit_with_version(version, is_quiet=False):
    if not is_quiet:
        print("version: {0}".format(version))
    sys.exit(0)


def _exit_with_default_config(is_quiet=False):
    if not is_quiet:
        pkg_root = os.path.dirname(__file__)
        default_config_filename = os.path.join(pkg_root, "data", ".howfairis.yml")
        with open(default_config_filename, "rt") as f:
            text = f.read()
        print(text)
    sys.exit(0)


def _print_feedback_about_config_args(ignore_repo_config, repo_config_filename, user_config_filename, is_quiet=False):

    if ignore_repo_config is True and is_quiet is False:
        print("Ignoring any configuration files on the remote.")

    if ignore_repo_config is True:
        assert repo_config_filename is None, "When ignoring any configuration files on the remote, you" + \
                                             " should not set a remote configuration filename."

    if ignore_repo_config is False and repo_config_filename is not None and is_quiet is False:
        print("Remote configuration filename: " + repo_config_filename)

    if user_config_filename is not None:
        print("Local configuration file: " + user_config_filename)


def _print_feedback_about_repo_args(url, branch, path, is_quiet=False):

    assert url is not None, "Expected URL to not be emtpy."

    if not is_quiet:
        print("Checking compliance with fair-software.eu...")

        if url is not None:
            print("url: " + url)

        if branch is not None:
            print("branch: " + branch)

        if path is not None:
            print("path: " + path)


# pylint: disable=too-many-arguments
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("-b", "--branch", default=None, type=click.STRING,
              help="Which git branch to use. Also accepts other git references like SHA or tag.")
@click.option("-c", "--user-config-filename", default=None, type=click.Path(),
              help="Name of the configuration file to control howfairis'es behavior. The configuration " +
                   "file needs to be present on the local system and can include a relative path.")
@click.option("-d", "--show-default-config", default=False, is_flag=True,
              help="Show default configuration and exit.")
@click.option("-i", "--ignore-repo-config", default=False, is_flag=True,
              help="Ignore any configuration files on the remote.")
@click.option("-p", "--path", default=None, type=click.STRING,
              help="Relative path (on the remote). Use this if you want howfairis to look for a " +
                   "README and a configuration file in a subdirectory.")
@click.option("-q", "--quiet", default=False, is_flag=True,
              help="Use this flag to disable all printing except errors.")
@click.option("-r", "--repo-config-filename", default=None, type=click.STRING,
              help="Name of the configuration file to control howfairis'es behavior. The configuration " +
                   "file needs to be on the remote, and takes into account the value of " +
                   "--branch and --path. Default: .howfairis.yml")
@click.option("-t", "--show-trace", default=False, is_flag=True,
              help="Use this flag to show the full traceback when errors occur.")
@click.option("-v", "--version", default=False, is_flag=True,
              help="Use this flag to print howfairis'es version and exit.")
@click.argument("url", required=False)
def cli(url=None, branch=None, user_config_filename=None, repo_config_filename=None, path=None,
        show_trace=False, version=False, ignore_repo_config=False, show_default_config=False, quiet=False):

    """Determine compliance with recommendations from fair-software.eu for the GitHub or GitLab repository at URL."""
    if show_trace is False:
        sys.tracebacklimit = 0

    if version is True:
        _exit_with_version(__version__, is_quiet=quiet)

    if show_default_config is True:
        _exit_with_default_config(is_quiet=quiet)

    _print_feedback_about_repo_args(url, branch, path, is_quiet=quiet)
    _print_feedback_about_config_args(ignore_repo_config, repo_config_filename, user_config_filename, is_quiet=quiet)

    init_terminal_colors()
    repo = Repo(url, branch, path)
    checker = Checker(repo, user_config_filename=user_config_filename, repo_config_filename=repo_config_filename,
                      ignore_repo_config=ignore_repo_config, is_quiet=quiet)

    previous_compliance = checker.readme.get_compliance()
    current_compliance = checker.check_five_recommendations()

    _exit_with_call_to_action(previous_compliance, current_compliance, checker.readme, is_quiet=quiet)


if __name__ == "__main__":
    cli()
