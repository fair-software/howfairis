import os
import sys
import click
from colorama import init as init_terminal_colors
from howfairis.__version__ import __version__
from howfairis.checker import Checker
from howfairis.repo import Repo


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
@click.option("-r", "--repo-config-filename", default=None, type=click.STRING,
              help="Name of the configuration file to control howfairis'es behavior. The configuration " +
                   "file needs to be on the remote, and takes into account the value of " +
                   "--branch and --path. Default: .howfairis.yml")
@click.option("-t", "--show-trace", default=False, is_flag=True,
              help="Show full traceback on errors.")
@click.option("-v", "--version", default=False, is_flag=True,
              help="Show version and exit.")
@click.argument("url", required=False)
def cli(url=None, branch=None, user_config_filename=None, repo_config_filename=None, path=None,
        show_trace=False, version=False, ignore_repo_config=False, show_default_config=False):
    # pylint: disable=too-many-locals

    """Determine compliance with recommendations from fair-software.eu for the GitHub or GitLab repository at URL."""

    if version is True:
        print("version: {0}".format(__version__))
        return

    if show_default_config is True:
        pkg_root = os.path.dirname(__file__)
        default_config_filename = os.path.join(pkg_root, "data", ".howfairis.yml")
        with open(default_config_filename, "rt") as f:
            text = f.read()
        print(text)
        return

    if show_trace is False:
        sys.tracebacklimit = 0

    init_terminal_colors()
    assert url is not None, "Expected URL to not be emtpy."
    print("Checking compliance with fair-software.eu...")

    if url is not None:
        print("url: " + url)

    if branch is not None:
        print("branch: " + branch)

    if path is not None:
        print("path: " + path)

    if ignore_repo_config is True:
        print("Ignoring any configuration files on the remote.")
        assert repo_config_filename is None, "When ignoring any configuration files on the remote, you" + \
                                             " should not set a remote configuration filename."
    else:
        if repo_config_filename is not None:
            print("Remote configuration filename: " + repo_config_filename)

    if user_config_filename is not None:
        print("Local configuration file: " + user_config_filename)

    repo = Repo(url, branch, path)

    checker = Checker(repo, user_config_filename, repo_config_filename, ignore_repo_config)
    current_compliance = checker.check_five_recommendations()
    badge = current_compliance.calc_badge(checker.readme.fmt)

    print("\nCalculated compliance: " + " ".join(current_compliance.as_unicode()) + "\n")

    if checker.readme.text is None:
        sys.exit(1)

    previous_compliance = checker.readme.get_compliance()

    if previous_compliance is None:
        print("It seems you have not yet added the fair-software.eu badge to " +
              "your {0}. You can do so by pasting the following snippet:\n\n{1}"
              .format(checker.readme.filename, badge))
        sys.exit(1)

    if current_compliance == previous_compliance:
        print("Expected badge is equal to the actual badge. It's all good.\n")
        sys.exit(0)

    if current_compliance.count() > previous_compliance.count():
        print("Congratulations! The compliance of your repository exceeds " +
              "the current fair-software.eu badge in your " +
              "{0}. You can replace it with the following snippet:\n\n{1}"
              .format(checker.readme.filename, badge))
        sys.exit(1)

    print("The compliance of your repository is different from the current " +
          "fair-software.eu badge in your " +
          "{0}. Please replace it with the following snippet:\n\n{1}"
          .format(checker.readme.filename, badge))

    sys.exit(1)


if __name__ == "__main__":
    cli()
