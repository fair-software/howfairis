from tests.contracts.Repo import Contract
import unittest
import requests_mock
import requests


class RepoTest(Contract, unittest.TestCase):

    @requests_mock.Mocker()
    def test_url(self, m):
        m.get('http://test.com', text='resp')
        text = requests.get('http://test.com').text
        assert text == 'resp', "Nope"
