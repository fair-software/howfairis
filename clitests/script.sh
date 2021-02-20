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
howfairis https://github.com/fair-software/badge-test -p force/00100
howfairis https://github.com/fair-software/badge-test -p force/10110
howfairis https://github.com/fair-software/badge-test -p force/11110
howfairis https://github.com/fair-software/badge-test -p force/11111
howfairis https://github.com/fair-software/badge-test -p force/uu1uu
howfairis https://github.com/fair-software/badge-test -p ignore_commented_badges


# gitlab
howfairis https://gitlab.com/jspaaks/badge-test
howfairis https://gitlab.com/jspaaks/badge-test -p force/00100
howfairis https://gitlab.com/jspaaks/badge-test -p force/10110
howfairis https://gitlab.com/jspaaks/badge-test -p force/11110
howfairis https://gitlab.com/jspaaks/badge-test -p force/11111
howfairis https://gitlab.com/jspaaks/badge-test -p force/uu1uu
howfairis https://gitlab.com/jspaaks/badge-test -p ignore_commented_badges
