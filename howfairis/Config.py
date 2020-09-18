import os
import requests
from ruamel.yaml import YAML
from howfairis.schema import validate_against_schema


class Config:
    def __init__(self, repo, config_filename=None, include_comments=None):
        self.repo = repo
        self.has_user_input = config_filename is not None
        self.yamldata = None

        self._load_default_config()
        self._load_repo_config(config_filename)
        self._load_cli_config(include_comments)

    def _load_cli_config(self, include_comments):
        if include_comments == "yes":
            d = dict(include_comments=True)
        elif include_comments == "no":
            d = dict(include_comments=False)
        else:
            d = dict()
        self.yamldata.update(d)
        return self

    def _load_default_config(self):

        pkg_root = os.path.dirname(__file__)
        config_filename = os.path.join(pkg_root, "data", ".howfairis.yml")
        with open(config_filename, "rt") as f:
            text = f.read()
        newdata = YAML(typ="safe").load(text)
        if newdata is None:
            newdata = dict()
        try:
            validate_against_schema(newdata)
        except Exception as e:
            raise Exception("Default configuration file should follow the schema.") from e
        self.yamldata = newdata
        return self

    def _load_repo_config(self, config_filename):
        if self.repo is None:
            return self

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
            newdata = YAML(typ="safe").load(response.text)
        except Exception as e:
            raise Exception("Problem loading YAML configuration from file {0}".format(raw_url)) from e

        try:
            validate_against_schema(newdata)
        except Exception as e:
            raise Exception("Configuration file should follow the schema.") from e

        self.yamldata.update(newdata)

        return self
