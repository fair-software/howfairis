def print_feedback_about_repo_args(url, branch, path, is_quiet=False):

    assert url is not None, "Expected URL to not be emtpy."

    if not is_quiet:
        print("Checking compliance with fair-software.eu...")

        if url is not None:
            print("url: " + url)

        if branch is not None:
            print("branch: " + branch)

        if path is not None:
            print("path: " + path)
