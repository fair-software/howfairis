import os
import requests
from ruamel.yaml import YAML
from voluptuous.error import Invalid
from voluptuous.error import MultipleInvalid
from howfairis.schema import validate_against_schema


class Config:
    def __init__(self, repo, config_filename=None, ignore_remote_config=False):
        self.default = Config._load_default_config()
        self.repo = Config._load_repo_config(repo, ignore_remote_config)
        self.user = Config._load_user_config(config_filename)

    @staticmethod
    def _load_default_config():
        pkg_root = os.path.dirname(__file__)
        config_filename = os.path.join(pkg_root, "data", ".howfairis.yml")
        with open(config_filename, "rt") as f:
            text = f.read()
        default_config = YAML(typ="safe").load(text)
        if default_config is None:
            default_config = dict()
        try:
            validate_against_schema(default_config)
        except (Invalid, MultipleInvalid):
            print("Default configuration file should follow the schema for it to be considered.")
            return dict()
        return default_config

    @staticmethod
    def _load_repo_config(repo, ignore_remote_config):
        if repo is None:
            return dict()

        if ignore_remote_config is True:
            return dict()

        if repo.config_file is None:
            config_filename = ".howfairis.yml"
        else:
            config_filename = repo.config_file

        raw_url = repo.raw_url_format_string.format(config_filename)
        try:
            response = requests.get(raw_url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            print("Using the configuration file {0}".format(raw_url))
        except requests.HTTPError as e:
            if repo.config_file is not None:
                raise Exception("Could not find the configuration file {0}".format(raw_url)) from e
            return dict()

        try:
            repo_config = YAML(typ="safe").load(response.text)
        except Exception as e:
            raise Exception("Problem loading YAML configuration from file {0}".format(raw_url)) from e

        try:
            validate_against_schema(repo_config)
        except (Invalid, MultipleInvalid):
            print("Repository's configuration file should follow the schema for it to be considered.")
            return dict()

        return repo_config

    @staticmethod
    def _load_user_config(config_filename):
        if config_filename is None:
            return dict()

        p = os.path.join(os.getcwd(), config_filename)
        if not os.path.exists(p):
            raise FileNotFoundError("{0} doesn't exist.".format(config_filename))

        with open(p, "rt") as f:
            text = f.read()
        user_config = YAML(typ="safe").load(text)
        if user_config is None:
            user_config = dict()
        try:
            validate_against_schema(user_config)
        except Exception as e:
            raise Exception("User configuration file should follow the schema.") from e
        return user_config

    @property
    def merged(self):
        m = dict()
        m.update(self.default)
        m.update(self.repo)
        m.update(self.user)
        return m
