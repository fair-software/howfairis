def print_feedback_about_repo_args(url, branch, self_hosted, path, is_quiet=False):
    """  """

    assert url is not None, "Expected URL to not be emtpy."

    if not is_quiet:
        print("Checking compliance with fair-software.eu...")

        if url is not None:
            print("url: " + url)

        if self_hosted:
            print("using self-hosted instance")

        if branch is not None:
            print("branch: " + branch)

        if path is not None:
            print("path: " + path)
