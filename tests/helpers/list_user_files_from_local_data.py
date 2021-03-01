from .list_files_from_local_data import list_files_from_local_data


def list_user_files_from_local_data(who_is_asking_file):
    return list_files_from_local_data(who_is_asking_file, dir_type="user")
