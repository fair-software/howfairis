#!/usr/bin/env bash

# exit when any command fails
set -e

which howfairis
howfairis --help
howfairis --version
howfairis https://github.com/fair-software/badge-test
howfairis https://github.com/fair-software/badge-test -p force/00100
howfairis https://github.com/fair-software/badge-test -p force/10110
howfairis https://github.com/fair-software/badge-test -p force/11110
howfairis https://github.com/fair-software/badge-test -p force/11111
howfairis https://github.com/fair-software/badge-test -p force/uu1uu
howfairis https://github.com/fair-software/badge-test -p force/u
howfairis https://github.com/fair-software/badge-test -p include_comments
