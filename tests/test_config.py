from requests_mock import Mocker

from howfairis import Config, Repo


def test_config_withoutrepoconfig_shouldusedefault(requests_mock: Mocker):
    requests_mock.get("https://api.github.com/repos/fair-software/howfairis", json={"default_branch": "master"} )
    requests_mock.get("https://raw.githubusercontent.com/fair-software/howfairis/master/.howfairis.yml", status_code=404)
    repo = Repo("https://github.com/fair-software/howfairis")
    config = Config(repo)

    assert config.force_checklist is None, "config not same as `howfairis/data/.howfairis.yml`"
    assert config.force_citation is None, "config not same as `howfairis/data/.howfairis.yml`"
    assert config.force_license is None, "config not same as `howfairis/data/.howfairis.yml`"
    assert config.force_registry is None, "config not same as `howfairis/data/.howfairis.yml`"
    assert config.force_citation is None, "config not same as `howfairis/data/.howfairis.yml`"
    assert config.force_checklist is None, "config not same as `howfairis/data/.howfairis.yml`"
    assert config.include_comments is False, "config not same as `howfairis/data/.howfairis.yml`"
