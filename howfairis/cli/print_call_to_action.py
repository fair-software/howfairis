from howfairis.code_repository_platforms import Platform
from howfairis.workarounds.github_caching import github_caching_check


def print_call_to_action(previous_compliance, current_compliance, checker, is_quiet=False):
    """  """
    if checker.readme.text is None:
        return 1

    badge = current_compliance.calc_badge(checker.readme.file_format)

    if previous_compliance is None:
        message = "It seems you have not yet added the fair-software.eu badge to " + \
                  f"your {checker.readme.filename}. You can do so by pasting the following snippet:\n\n{badge}"
        sys_exit_code = 1

    elif current_compliance == previous_compliance:
        message = "Expected badge is equal to the actual badge. It's all good.\n"
        sys_exit_code = 0

    elif current_compliance.count() > previous_compliance.count():
        message = "Congratulations! The compliance of your repository exceeds " + \
                  "the current fair-software.eu badge in your " + \
                  f"{checker.readme.filename}. You can replace it with the following snippet:\n\n{badge}"
        sys_exit_code = 1

    else:
        message = "The compliance of your repository is different from the current " + \
                  "fair-software.eu badge in your " + \
                  f"{checker.readme.filename}. Please replace it with the following snippet:\n\n{badge}"
        sys_exit_code = 1

    if not is_quiet:
        print("\nCalculated compliance: " + " ".join(current_compliance.as_unicode()) + "\n")
        print(message)
        if checker.repo.platform == Platform.GITHUB:
            github_caching_check(checker)

    return sys_exit_code


def automate_call_to_action(previous_compliance, current_compliance, checker, is_quiet=False):
    """ Function to automate the process of updating the fair-software.eu badge """
    if checker.readme.text is None:
        return 1

    if previous_compliance is None:
        badge = current_compliance.calc_badge(checker.readme.file_format)
        message = "It seems you have not yet added the fair-software.eu badge to " + \
                  f"your {checker.readme.filename}. You can do so by pasting the following snippet:\n\n{badge}"
        sys_exit_code = 1

    elif current_compliance == previous_compliance:
        message = "Expected badge is equal to the actual badge. It's all good.\n"
        sys_exit_code = 0

    else:
        message = "Repository has a fair-software.eu badge, but current compliance does not match the badge\n" + \
                  f"Updating badge image URL in {checker.readme.filename}."
        with open(checker.readme.filename, "r", encoding="utf8") as readme:
            readme_contents = readme.read()
        readme_contents = readme_contents.replace(previous_compliance.badge_image_url(),
                                                  current_compliance.badge_image_url())
        with open(checker.readme.filename, "w", encoding="utf8") as readme:
            readme.write(readme_contents)
        sys_exit_code = 0

    if not is_quiet:
        print("\nCalculated compliance: " + " ".join(current_compliance.as_unicode()) + "\n")
        print(message)
        if checker.repo.platform == Platform.GITHUB:
            github_caching_check(checker)

    return sys_exit_code
