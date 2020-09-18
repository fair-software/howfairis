#!/usr/bin/env bash

# exit when any command fails
set -e

# For character encoding on Windows
export PYTHONIOENCODING=UTF-8

which howfairis
howfairis --help
howfairis --version

DURATION=10

# github
howfairis https://github.com/fair-software/badge-test && sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/00100 && sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/10110 && sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/11110 && sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/11111 && sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/uu1uu && sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/u && sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p include_comments && sleep $DURATION


# gitlab
howfairis https://gitlab.com/jspaaks/badge-test && sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/00100 && sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/10110 && sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/11110 && sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/11111 && sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/uu1uu && sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/u && sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p include_comments && sleep $DURATION
