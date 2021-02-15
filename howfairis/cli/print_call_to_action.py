def print_call_to_action(previous_compliance, current_compliance, readme, is_quiet=False):

    badge = current_compliance.calc_badge(readme.file_format)

    if not is_quiet:
        print("\nCalculated compliance: " + " ".join(current_compliance.as_unicode()) + "\n")

    if previous_compliance is None:
        if not is_quiet:
            print("It seems you have not yet added the fair-software.eu badge to " +
                  "your {0}. You can do so by pasting the following snippet:\n\n{1}"
                  .format(readme.filename, badge))
        return 1

    if current_compliance == previous_compliance:
        if not is_quiet:
            print("Expected badge is equal to the actual badge. It's all good.\n")
        return 0

    if current_compliance.count() > previous_compliance.count():
        if not is_quiet:
            print("Congratulations! The compliance of your repository exceeds " +
                  "the current fair-software.eu badge in your " +
                  "{0}. You can replace it with the following snippet:\n\n{1}"
                  .format(readme.filename, badge))
        return 1

    if not is_quiet:
        print("The compliance of your repository is different from the current " +
              "fair-software.eu badge in your " +
              "{0}. Please replace it with the following snippet:\n\n{1}"
              .format(readme.filename, badge))

    return 1
