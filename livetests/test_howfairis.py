#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the howfairis module.
"""
import requests
import time
import random
from howfairis import Checker
from howfairis import Config
from howfairis import Repo


def test_heavy_handed_livetest_rsd():
    software_api_url = "https://www.research-software.nl/api/software?isPublished=true"
    try:
        response = requests.get(software_api_url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError:
        print("Unable to retrieve the list of URLs")
        return False

    urls = []
    for d in response.json():
        for key, values in d["repositoryURLs"].items():
            urls.extend(values)

    random.shuffle(urls)
    for url in urls[:25]:
        print(url)
        repo = Repo(url)
        config = Config(repo)
        checker = Checker(config, repo).check_five_recommendations()
        for c in checker.compliance:
            assert isinstance(c, bool)

        # sleep to avoid rate limiting of GitHub API
        time.sleep(20)
