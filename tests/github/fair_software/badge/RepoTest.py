from tests.contracts.Repo import Contract
from howfairis import Repo
import unittest
import requests_mock
from tests.github.fair_software.badge.mocks import get_mocked_responses


class RepoTest(Contract, unittest.TestCase):

    def test_api(self):
        with requests_mock.Mocker() as mocker:
            for args, kwargs in get_mocked_responses():
                mocker.get(*args, **kwargs)
            actual_repo = Repo("https://github.com/fair-software/badge")
            assert actual_repo.api == "https://api.github.com/repos/fair-software/badge", "TODO"

    def test_branch(self):
        with requests_mock.Mocker() as mocker:
            for args, kwargs in get_mocked_responses():
                mocker.get(*args, **kwargs)
            actual_repo = Repo("https://github.com/fair-software/badge")
            assert actual_repo.branch is None, "TODO"

    def test_default_branch(self):
        with requests_mock.Mocker() as mocker:
            for args, kwargs in get_mocked_responses():
                mocker.get(*args, **kwargs)
            actual_repo = Repo("https://github.com/fair-software/badge")
            assert actual_repo.default_branch == "master", "TODO"

    def test_url(self):
        with requests_mock.Mocker() as mocker:
            for args, kwargs in get_mocked_responses():
                mocker.get(*args, **kwargs)
            actual_repo = Repo("https://github.com/fair-software/badge")
            assert actual_repo.url == "https://github.com/fair-software/badge", "TODO"
