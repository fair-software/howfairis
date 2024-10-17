#!/usr/bin/env python

"""Tests for the howfairis module.
"""
import random
import pytest
import requests
from howfairis import Checker
from howfairis import Repo
from howfairis import Compliance


def get_urls(n=None):
    software_api_url = "https://research-software-directory.org/api/v1/repository_url"
    try:
        response = requests.get(software_api_url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except requests.HTTPError:
        print("Unable to retrieve the list of URLs")
        return False

    urls = []
    for _repo in response.json():
        if _repo["url"].startswith(("https://github.com", "https://gitlab.com")):
            urls.append(_repo["url"])
    if n is None:
        return random.shuffle(urls)
    else:
        random.shuffle(urls)
        return urls[:n]


@pytest.fixture(params=get_urls(5))
def url_fixture(request):
    return request.param


def test_heavy_handed_testing_of_rsd_urls(url_fixture):
    repo = Repo(url_fixture)
    checker = Checker(repo)
    compliance = checker.check_five_recommendations()
    assert isinstance(compliance, Compliance)
