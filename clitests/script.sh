#!/usr/bin/env bash


eval_and_print_status () {
   if [ -n "$CI" ]
   then
      # has CI env var
      echo "$1"
      echo "::group::output"
      eval "$1"
      echo "::endgroup::"
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
SLEEP_DURATION=20
eval_and_print_status "howfairis https://github.com/fair-software/howfairis-livetest"
eval_and_print_status "howfairis https://github.com/fair-software/howfairis-livetest -p skipping/00100"
eval_and_print_status "howfairis https://github.com/fair-software/howfairis-livetest -p skipping/10110"
eval_and_print_status "howfairis https://github.com/fair-software/howfairis-livetest -p skipping/11110"
eval_and_print_status "howfairis https://github.com/fair-software/howfairis-livetest -p skipping/11111"
eval_and_print_status "howfairis https://github.com/fair-software/howfairis-livetest -p skipping/uu1uu"
eval_and_print_status "howfairis https://github.com/fair-software/howfairis-livetest -p ignore_commented_badges"

# gitlab
SLEEP_DURATION=0
eval_and_print_status "howfairis https://gitlab.com/jspaaks/howfairis-livetest"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/howfairis-livetest -p skipping/00100"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/howfairis-livetest -p skipping/10110"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/howfairis-livetest -p skipping/11110"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/howfairis-livetest -p skipping/11111"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/howfairis-livetest -p skipping/uu1uu"
eval_and_print_status "howfairis https://gitlab.com/jspaaks/howfairis-livetest -p ignore_commented_badges"

echo "All commands succeeded."
exit 0
