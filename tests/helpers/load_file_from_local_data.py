import os


def load_file_from_local_data(fname, who_is_asking_file):

    parent_dir = os.path.dirname(os.path.realpath(who_is_asking_file))
    fullpath = os.path.join(parent_dir, "data", fname)
    with open(fullpath, "rt") as fid:
        return fid.read()
