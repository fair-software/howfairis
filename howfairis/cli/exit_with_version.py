import sys


def exit_with_version(version, is_quiet=False):
    if not is_quiet:
        print("version: {0}".format(version))
    sys.exit(0)
