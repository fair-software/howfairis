import os


def load_files_from_local_data(who_is_asking_file):

    parent_dir = os.path.dirname(os.path.realpath(who_is_asking_file))
    data_dir = os.path.join(parent_dir, "data")

    files_dict = dict()
    for root, _, filenames in os.walk(data_dir):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            key = "/".join(fullpath.replace(data_dir, "").split(os.sep))
            with open(fullpath, "rt") as fid:
                files_dict[key] = fid.read()

    return files_dict
