import os


def print_default_config(is_quiet=False):
    if not is_quiet:
        parent_dir = os.path.dirname(__file__)
        pkg_root = os.path.join(parent_dir, "..")
        default_config_filename = os.path.join(pkg_root, "data", ".howfairis.yml")
        with open(default_config_filename, "rt") as f:
            text = f.read()
        print(text, end='')
    return 0
