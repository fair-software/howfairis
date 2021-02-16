from howfairis.workarounds.github_caching import github_caching_check


def print_call_to_action(previous_compliance, current_compliance, checker, is_quiet=False):

    badge = current_compliance.calc_badge(checker.readme.file_format)

    if not is_quiet:
        print("\nCalculated compliance: " + " ".join(current_compliance.as_unicode()) + "\n")

    sys_exit_code = 1
    if previous_compliance is None:
        if not is_quiet:
            print("It seems you have not yet added the fair-software.eu badge to " +
                  "your {0}. You can do so by pasting the following snippet:\n\n{1}"
                  .format(checker.readme.filename, badge))

    elif current_compliance == previous_compliance:
        if not is_quiet:
            print("Expected badge is equal to the actual badge. It's all good.\n")
        sys_exit_code = 0

    elif current_compliance.count() > previous_compliance.count():
        if not is_quiet:
            print("Congratulations! The compliance of your repository exceeds " +
                  "the current fair-software.eu badge in your " +
                  "{0}. You can replace it with the following snippet:\n\n{1}"
                  .format(checker.readme.filename, badge))

    elif not is_quiet:
        print("The compliance of your repository is different from the current " +
              "fair-software.eu badge in your " +
              "{0}. Please replace it with the following snippet:\n\n{1}"
              .format(checker.readme.filename, badge))
        github_caching_check(checker)

    return sys_exit_code
