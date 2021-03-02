from .list_files_from_local_data import list_files_from_local_data


def load_files_from_local_data(who_is_asking_file, dir_type):
    files_dict = dict()
    for key, fullpath in list_files_from_local_data(who_is_asking_file, dir_type).items():
        with open(fullpath, "rt", encoding='utf-8') as fid:
            files_dict[key] = fid.read()

    return files_dict
