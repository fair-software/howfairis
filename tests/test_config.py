from howfairis import Config, Repo


def test_default():
    repo = Repo('https://github.com/fair-software/does-not-exist')
    config = Config(repo)

    expected = {'force_checklist': None,
                'force_citation': None,
                'force_license': None,
                'force_registry': None,
                'force_repository': None,
                'include_comments': False}
    assert config.merged == expected, 'config not same as `howfairis/data/.howfairis.yml`'
