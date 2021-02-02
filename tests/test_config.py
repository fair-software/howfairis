from requests_mock import Mocker

from howfairis import Config, Repo


def test_config_withoutrepoconfig_shouldusedefault(requests_mock: Mocker):
    requests_mock.get('https://api.github.com/repos/fair-software/howfairis', json={'default_branch': 'master'} )
    requests_mock.get('https://raw.githubusercontent.com/fair-software/howfairis/master/.howfairis.yml', status_code=404)
    repo = Repo('https://github.com/fair-software/howfairis')
    config = Config(repo)

    expected = {'force_checklist': None,
                'force_citation': None,
                'force_license': None,
                'force_registry': None,
                'force_repository': None,
                'include_comments': False}
    assert config.merged == expected, 'config not same as `howfairis/data/.howfairis.yml`'
