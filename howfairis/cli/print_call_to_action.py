from howfairis.code_repository_platforms import Platform
from howfairis.workarounds.github_caching import github_caching_check


def print_call_to_action(previous_compliance, current_compliance, checker, is_quiet=False):
    """  """
    if checker.readme.text is None:
        return 1

    message = "Failed to compare current and previous compliance."
    sys_exit_code = 1

    if checker.repo.platform == Platform.GITHUB:
        badge = current_compliance.calc_badge(checker.readme.file_format)
        badge_location = f"{checker.readme.filename}"

        if previous_compliance["readme"] is None:
            message = "It seems you have not yet added the fair-software.eu badge to " + \
                      f"your {checker.readme.filename}. You can do so by pasting the following snippet:\n\n{badge}"
            sys_exit_code = 1

        elif current_compliance == previous_compliance["readme"]:
            message = "Expected badge is equal to the actual badge. It's all good.\n"
            sys_exit_code = 0

        elif current_compliance.count() > previous_compliance["readme"].count():
            message = "Congratulations! The compliance of your repository exceeds " + \
                      "the current fair-software.eu badge in your " + \
                      f"{checker.readme.filename}. You can replace it with the following snippet:\n\n{badge}"
            sys_exit_code = 1

        else:
            message = "The compliance of your repository is different from the current " + \
                      "fair-software.eu badge in your " + \
                      f"{checker.readme.filename}. Please replace it with the following snippet:\n\n{badge}"
            sys_exit_code = 1

    elif checker.repo.platform == Platform.GITLAB:
        badge_location = f"{checker.readme.filename} or GitLab badges"
        readme_badge = current_compliance.calc_badge(checker.readme.file_format)
        project_badge = current_compliance.calc_badge(checker.badges.file_format)

        if previous_compliance["readme"] is None and previous_compliance["badges"] is None:
            message = "It seems you have not yet added the fair-software.eu badge to " + \
                      f"your {checker.readme.filename} or project badges. You can do so by pasting the following " + \
                      f"snippet:\n\n{readme_badge}\n\nor adding project settings\n{project_badge}"
            sys_exit_code = 1

        elif (
                (current_compliance == previous_compliance["readme"] and current_compliance == previous_compliance["badges"])
                or (current_compliance == previous_compliance["readme"] and previous_compliance["badges"] is None)
                or (previous_compliance["readme"] is None and current_compliance == previous_compliance["badges"])
             ):
            message = "Expected badge is equal to the actual badge(s). It's all good.\n"
            sys_exit_code = 0

        elif previous_compliance["readme"] is None or previous_compliance["badges"] is None:
            if previous_compliance["readme"] is None and current_compliance.count() > previous_compliance["badges"].count():
                message = "Congratulations! The compliance of your repository exceeds " + \
                          "the current fair-software.eu badge in your " + \
                          f"project badges. You can adjust the project settings to\n{project_badge}"
                sys_exit_code = 1

            elif current_compliance.count() > previous_compliance["readme"] and previous_compliance["badges"] is None:
                message = "Congratulations! The compliance of your repository exceeds " + \
                          "the current fair-software.eu badge in your " + \
                          f"{checker.readme.filename}. You can replace it with the following " + \
                          f"snippet:\n\n{readme_badge}"
                sys_exit_code = 1

        elif (current_compliance.count() > previous_compliance["readme"] or current_compliance.count() > previous_compliance["badges"].count()):
            message = "Congratulations! The compliance of your repository exceeds " + \
                      "the current fair-software.eu badge in your " + \
                      f"{checker.readme.filename} or project badges. You can replace it with the following " + \
                      f"snippet:\n\n{readme_badge}\n\nor adjusting the project settings to\n{project_badge}"
            sys_exit_code = 1

        else:
            message = "The compliance of your repository is different from the current " + \
                      "fair-software.eu badge in your " + \
                      f"{checker.readme.filename} or project badges. Please replace it with the following snippet:\n\n{badge}" + \
                      f"or adjust the project settings to\n{project_badge}"
            sys_exit_code = 1

    if not is_quiet:
        print("\nCalculated compliance: " + " ".join(current_compliance.as_unicode()) + "\n")
        print(message)
        if checker.repo.platform == Platform.GITHUB:
            github_caching_check(checker)

    return sys_exit_code
