#!/usr/bin/env bash

# exit when any command fails
set -e

# For character encoding on Windows
export PYTHONIOENCODING=UTF-8

which howfairis
howfairis --help
howfairis --version
howfairis --show-default-config

DURATION=20

# github
howfairis https://github.com/fair-software/badge-test
sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/00100
sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/10110
sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/11110
sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/11111
sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p force/uu1uu
sleep $DURATION
howfairis https://github.com/fair-software/badge-test -p ignore_commented_badges
sleep $DURATION


# gitlab
howfairis https://gitlab.com/jspaaks/badge-test
sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/00100
sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/10110
sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/11110
sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/11111
sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p force/uu1uu
sleep $DURATION
howfairis https://gitlab.com/jspaaks/badge-test -p ignore_commented_badges
