from howfairis.code_repository_platforms import Platform
from howfairis.workarounds.github_caching import github_caching_check


def print_call_to_action(previous_compliance, current_compliance, checker, is_quiet=False):

    if checker.readme.text is None:
        return 1

    badge = current_compliance.calc_badge(checker.readme.file_format)

    if previous_compliance is None:
        message = ("It seems you have not yet added the fair-software.eu badge to " +
                   "your {0}. You can do so by pasting the following snippet:\n\n{1}"
                   .format(checker.readme.filename, badge))
        sys_exit_code = 1

    elif current_compliance == previous_compliance:
        message = "Expected badge is equal to the actual badge. It's all good.\n"
        sys_exit_code = 0

    elif current_compliance.count() > previous_compliance.count():
        message = ("Congratulations! The compliance of your repository exceeds " +
                   "the current fair-software.eu badge in your " +
                   "{0}. You can replace it with the following snippet:\n\n{1}"
                   .format(checker.readme.filename, badge))
        sys_exit_code = 1

    else:
        message = ("The compliance of your repository is different from the current " +
                   "fair-software.eu badge in your " +
                   "{0}. Please replace it with the following snippet:\n\n{1}"
                   .format(checker.readme.filename, badge))
        sys_exit_code = 1

    if not is_quiet:
        print("\nCalculated compliance: " + " ".join(current_compliance.as_unicode()) + "\n")
        print(message)
        if checker.repo.platform == Platform.GITHUB:
            github_caching_check(checker)

    return sys_exit_code
