from requests_mock import Mocker

from howfairis import Config, Repo


def test_default_config(requests_mock: Mocker):
    requests_mock.get('https://raw.githubusercontent.com/fair-software/does-not-exist/master/.howfairis.yml', status_code=404)
    repo = Repo('https://github.com/fair-software/does-not-exist')
    config = Config(repo)

    expected = {'force_checklist': None,
                'force_citation': None,
                'force_license': None,
                'force_registry': None,
                'force_repository': None,
                'include_comments': False}
    assert config.merged == expected, 'config not same as `howfairis/data/.howfairis.yml`'
