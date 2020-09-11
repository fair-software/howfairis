import sys
from colorama import init as init_terminal_colors
import click
from howfairis import HowFairIsChecker


@click.command()
@click.argument("url")
@click.option("-c", "--config-file", default=None, help="Config file. Default: .howfairis.yml", type=click.Path())
@click.option("-b", "--branch", default="master", help="Which git branch to use. Default: master")
@click.option("-p", "--path", default="", help="Relative path to the readme. Default: empty")
@click.option("-s", "--show-trace", default=False, help="Show full traceback on errors. Default: False", is_flag=True)
def cli(url, config_file=".howfairis.yml", branch=None, path=None, show_trace=False):
    """Determine compliance with recommendations from fair-software.eu for the GitHub repository at URL."""
    if show_trace is False:
        sys.tracebacklimit = 0
    init_terminal_colors()
    print("Checking compliance with fair-software.eu...")
    print("Running for {0}/{1}/{2}".format(url, branch, path.strip("/")))
    checker = HowFairIsChecker(url, config_file, branch, path)
    checker.check_five_recommendations()
    checker.check_badge()


if __name__ == "__main__":
    cli()
