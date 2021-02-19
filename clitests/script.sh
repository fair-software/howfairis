#!/usr/bin/env bash


eval_and_print_status () {
   if [ -n "$CI" ]
   then
      # has CI env var
      echo "$1"
      eval "$1"
   else
      # has no CI env var
      echo "       $1"
      eval "$1 &> /dev/null"
   fi

   if [ "$?" != "0" ]
   then
      tput cuu1
      echo "[FAIL] "
      exit 1
   fi
   tput cuu1
   echo "[PASS] "

   echo "sleeping for $SLEEP_DURATION seconds..."
   sleep $SLEEP_DURATION
   tput cuu1
   tput el
}

# For character encoding on Windows
export PYTHONIOENCODING=UTF-8
SLEEP_DURATION=20

echo "-------------------------------------------------------------------------"
echo "which howfairis:"
echo "-------------------------------------------------------------------------"
which howfairis
echo -e "\n\n"

echo "-------------------------------------------------------------------------"
echo "Print version:"
echo "-------------------------------------------------------------------------"
howfairis -v
echo -e "\n\n"

echo "-------------------------------------------------------------------------"
echo "Print help:"
echo "-------------------------------------------------------------------------"
howfairis --help
echo -e "\n\n"

echo "-------------------------------------------------------------------------"
echo "Print default configuration:"
echo "-------------------------------------------------------------------------"
howfairis --show-default-config
echo -e "\n\n"


# github
eval_and_print_status "howfairis https://github.com/fair-software/badge-test"
eval_and_print_status "howfairis https://github.com/fair-software/badge-test -p force/00100"
eval_and_print_status "howfairis https://github.com/fair-software/badge-test -p force/10110"
eval_and_print_status "howfairis https://github.com/fair-software/badge-test -p force/11110"
eval_and_print_status "howfairis https://github.com/fair-software/badge-test -p force/11111"
eval_and_print_status "howfairis https://github.com/fair-software/badge-test -p force/uu1uu"
eval_and_print_status "howfairis https://github.com/fair-software/badge-test -p ignore_commented_badges"

# gitlab
eval_and_print_status "howfairis https://gitlab.com/jspaaks/badge-test"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/badge-test -p force/00100"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/badge-test -p force/10110"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/badge-test -p force/11110"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/badge-test -p force/11111"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/badge-test -p force/uu1uu"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/badge-test -p ignore_commented_badges"

echo "All commands succeeded."
exit 0
