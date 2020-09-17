import os
import requests
import yaml
from howfairis.schema import validate_against_schema


class Config:
    def __init__(self, repo, config_filename=None, include_comments=None):
        self.repo = repo
        self.has_user_input = config_filename is not None
        self.yaml = None

        self._load_default_config()
        self._load_repo_config(config_filename)
        self._load_cli_config(include_comments)

    def _load_cli_config(self, include_comments=None):
        if include_comments is not None:
            d = dict(include_comments=include_comments)
            self.yaml.update(d)
        return self

    def _load_default_config(self):

        pkg_root = os.path.dirname(__file__)
        config_filename = os.path.join(pkg_root, "data", ".howfairis.yml")
        with open(config_filename, "rt") as f:
            text = f.read()
        data = yaml.safe_load(text)
        if data is None:
            data = dict()
        try:
            validate_against_schema(data)
        except Exception as e:
            raise Exception("Default configuration file should follow the schema.") from e
        self.yaml = data
        return self

    def _load_repo_config(self, config_filename):
        if config_filename is None:
            config_filename = ".howfairis.yml"

        raw_url = self.repo.raw_url_format_string.format(config_filename)
        try:
            response = requests.get(raw_url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            print("Using the configuration file {0}".format(raw_url))
        except requests.HTTPError as e:
            if self.has_user_input:
                raise Exception("Could not find the configuration file {0}".format(raw_url)) from e
            return self

        try:
            data = yaml.safe_load(response.text)
        except Exception as e:
            raise Exception("Problem loading YAML configuration from file {0}".format(raw_url)) from e

        try:
            validate_against_schema(data)
        except Exception as e:
            raise Exception("Configuration file should follow the schema.") from e

        self.yaml.update(data)

        return self

