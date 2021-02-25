from .load_files_from_local_data import load_files_from_local_data


def load_snippets_from_local_data(who_is_asking_file):
    return load_files_from_local_data(who_is_asking_file, dir_type="snippets")
