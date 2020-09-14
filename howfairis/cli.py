import sys
import click
import requests
from colorama import init as init_terminal_colors
from howfairis import HowFairIsChecker
from howfairis import __version__
from howfairis.ReadmeFormat import ReadmeFormat


def check_badge(compliance, readme=None, compliant_symbol="\u25CF", noncompliant_symbol="\u25CB"):

    if readme is None:
        readme = dict(filename=None, text=None, fmt=None)

    compliance_unicode = [None] * 5
    for i, c in enumerate(compliance):
        if c is True:
            compliance_unicode[i] = compliant_symbol
        else:
            compliance_unicode[i] = noncompliant_symbol

    compliance_string = "%20%20".join(
        [requests.utils.quote(symbol) for symbol in compliance_unicode])

    score = compliance.count(True)
    if score in [0, 1]:
        color_string = "red"
    elif score in [2, 3]:
        color_string = "orange"
    elif score in [4]:
        color_string = "yellow"
    elif score == 5:
        color_string = "green"

    badge_url = "https://img.shields.io/badge/fair--software.eu-{0}-{1}".format(compliance_string, color_string)
    if readme["fmt"] == ReadmeFormat.RESTRUCTUREDTEXT:
        badge = ".. image:: {0}\n   :target: {1}".format(badge_url, "https://fair-software.eu")
    if readme["fmt"] == ReadmeFormat.MARKDOWN:
        badge = "[![fair-software.eu]({0})]({1})".format(badge_url, "https://fair-software.eu")

    print("\nCalculated compliance: " + " ".join(compliance_unicode) + "\n")

    if readme["text"] is None:
        sys.exit(1)
    elif readme["text"].find(badge_url) == -1:
        print("While searching through your {0}, I did not find the expected badge:\n{1}"
              .format(readme["filename"], badge))
        sys.exit(1)
    else:
        print("Expected badge is equal to the actual badge. It's all good.\n")
        sys.exit(0)


# pylint: disable=too-many-arguments
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("-b", "--branch", default=None, type=click.STRING,
              help="Which git branch to use.")
@click.option("-c", "--config-file", default=None, type=click.Path(),
              help="Config file. Default: .howfairis.yml")
@click.option("-i", "--include-comments", default=False, is_flag=True,
              help="When looking for badges, include sections of the README that " +
              "have been commented out using <!-- and -->. Default: False")
@click.option("-p", "--path", default=None, type=click.STRING,
              help="Relative path. Use this if you want howfairis to look for a README in a subdirectory.")
@click.option("-s", "--show-trace", default=False, is_flag=True,
              help="Show full traceback on errors. Default: False")
@click.option("-v", "--version", default=False, is_flag=True,
              help="Show version.")
@click.argument("url", required=False)
def cli(url=None, branch=None, config_file=None, include_comments=False,
        path=None, show_trace=False, version=False):
    """Determine compliance with recommendations from fair-software.eu for the GitHub or GitLab repository at URL."""

    if version is True:
        print("version: {0}".format(__version__))
        return
    if show_trace is False:
        sys.tracebacklimit = 0

    init_terminal_colors()
    assert url is not None, "Expected URL to not be emtpy."
    print("Checking compliance with fair-software.eu...")
    print("url: " + url)
    if config_file is not None:
        print("config_file: " + config_file)
    if branch is not None:
        print("branch: " + branch)
    if path is not None:
        print("path: " + path)

    checker = HowFairIsChecker(url, config_file, branch, path, include_comments)
    checker.check_five_recommendations()
    check_badge(compliance=checker.compliance, readme=checker.readme)


if __name__ == "__main__":
    cli()
