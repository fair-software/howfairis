from howfairis.checker import DEFAULT_CONFIG_FILENAME


def print_feedback_about_config_args(ignore_repo_config, repo_config_filename, user_config_filename, is_quiet=False):

    if not is_quiet:
        if ignore_repo_config is True:
            print("Ignoring any configuration files on the remote.")

        if ignore_repo_config is False and repo_config_filename != DEFAULT_CONFIG_FILENAME:
            print("Remote configuration filename: " + repo_config_filename)

        if user_config_filename is not None:
            print("Local configuration file: " + user_config_filename)

    if ignore_repo_config is True:
        assert repo_config_filename is None, "When ignoring any configuration files on the remote, you" + \
                                             " should not set a remote configuration filename."
