# pylint: disable=too-many-arguments
import sys
import click
from colorama import init as init_terminal_colors
from howfairis import HowFairIsChecker
from howfairis import __version__


@click.command()
@click.option("-b", "--branch", default=None, help="Which git branch to use.")
@click.option("-c", "--config-file", default=None, help="Config file. Default: .howfairis.yml", type=click.Path())
@click.option("-p", "--path", default=None, help="Relative path. Use this if you want howfairis to look for " + \
                                                 "a README in a subdirectory.")
@click.option("-s", "--show-trace", default=False, help="Show full traceback on errors. Default: False", is_flag=True)
@click.option("-v", "--version", default=False, help="Show version.", is_flag=True)
@click.argument("url", nargs=-1)
def cli(url=None, config_file=None, branch=None,
        path=None, show_trace=False, version=False):
    """Determine compliance with recommendations from fair-software.eu for the GitHub or GitLab repository at URL."""

    if version is True:
        print("version: {0}".format(__version__))
        return
    if show_trace is False:
        sys.tracebacklimit = 0

    init_terminal_colors()

    if len(url) != 1:
        raise ValueError("Expected exactly one value for input argument URL.")

    print("Checking compliance with fair-software.eu...")
    print("url: " + url[0])
    if config_file is not None:
        print("config_file: " + config_file)
    if branch is not None:
        print("branch: " + branch)
    if path is not None:
        print("path: " + path)

    checker = HowFairIsChecker(url[0], config_file, branch, path)
    checker.check_five_recommendations()
    checker.check_badge()


if __name__ == "__main__":
    cli()
