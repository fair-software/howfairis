import os


def list_files_from_local_data(who_is_asking_file, dir_type):
    assert dir_type in ["repo", "user", "output"], "Argument dir_type should be either 'repo' or 'user' or 'output'."

    parent_dir = os.path.dirname(os.path.realpath(who_is_asking_file))

    d = {
        "repo": "repo-files",
        "user": "user-files",
        "output": "snippets"
    }[dir_type]

    data_dir = os.path.join(parent_dir, d)
    files_dict = dict()
    for root, _, filenames in os.walk(data_dir):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            key = "/".join(fullpath.replace(data_dir, "").split(os.sep))
            files_dict[key] = fullpath

    return files_dict


