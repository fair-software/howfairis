import os


def list_files_from_local_data(who_is_asking_file, dir_type):
    dir_types = ["frontend", "output", "repo", "user"]
    assert dir_type in dir_types, "Argument dir_type should be one of {0}".format(str(dir_types))

    parent_dir = os.path.dirname(os.path.realpath(who_is_asking_file))

    d = {
        "frontend": "frontend-files",
        "output": "snippets",
        "repo": os.path.join("..", "repo-files"),
        "user": os.path.join("..", "user-files")
    }[dir_type]

    data_dir = os.path.join(parent_dir, d)
    files_dict = dict()
    for root, _, filenames in os.walk(data_dir):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            key = "/".join(fullpath.replace(data_dir, "").split(os.sep))
            files_dict[key] = fullpath

    return files_dict


