# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- added, changed, removed of bleeding edge versus latest stable goes here

### Changed

- update supported Python versions to 3.11, 3.12, 3.13 [#372](https://github.com/fair-software/howfairis/pull/372)

## [0.14.2] - 2022-Sep-1

### Added

- added support for Python 3.10
- added timeouts to all `requests.get()` calls to avoid hanging behavior
- added `.dockerignore` to have smaller Docker context (< 0.5 MB instead of > 120MB)

### Changed

- updated `isort` related commands after it dropped its argument `--recursive`
- updated Pull Request template with specific instructions on how to create a clean testing environment and what tests to run
- updated cffconvert workflow after changes to the cffconvert GitHub Action
- minor changeas to the citation metadata
- updated the Dockerfile's FROM image to a more recent version of Alpine (3.16) and a more recent version of Python (3.10.6)
- fixed linter errors after reporting by prospector
- fixed bug in using gitlab credentials

# Removed

- dropped support for Python 3.6 (now end-of-life)
- removed `.zenodo.json` metadata file, Zenodo does not use it when you have a `CITATION.cff` file

## [0.14.1] - 2021-Mar-09

### Added

- Describe how to get api keys [#319](https://github.com/fair-software/howfairis/issues/319)
- Dont show cant-remove-comment warning for rst file without comments [#272](https://github.com/fair-software/howfairis/issues/272)

## [0.14.0] - 2021-Mar-02

### Added

- Can now ask instances of `Compliance` for their color [#301](https://github.com/fair-software/howfairis/issues/301)
- Can now ask instances of `Compliance` for their badge image url [#304](https://github.com/fair-software/howfairis/issues/304)
- Now optionally uses authenticated requests when making requests to github.com and gitlab.com
- Rate limits are now configurable and use exponential backoff and retry (adds [ratelimit](https://pypi.org/project/ratelimit/) and [backoff](https://pypi.org/project/backoff/) dependencies) [PR#286](https://github.com/fair-software/howfairis/pull/286)
- Now warns about GitHub's caching when using READMEs that were recently changed [PR#153](https://github.com/fair-software/howfairis/pull/153)
- Directory structure of tests was updated for conceptually more meaningful scenarios, improved consistency between platforms, and directory-level mocked API calls using `pytest`'s standard `conftest.py` pattern. [PR#285](https://github.com/fair-software/howfairis/pull/285)
- More tests, e.g. [PR#305](https://github.com/fair-software/howfairis/pull/305), [PR#293](https://github.com/fair-software/howfairis/pull/293)

## [0.13.0] - 2021-Feb-18

### Added
- docstrings for public API
- documentation hosted on readthedocs [#51](https://github.com/fair-software/howfairis/issues/51)
- code of conduct [#87](https://github.com/fair-software/howfairis/issues/87)
- contributing guide [#74](https://github.com/fair-software/howfairis/issues/74)
- Docker image [#62](https://github.com/fair-software/howfairis/issues/62)
- developer documentation [#83](https://github.com/fair-software/howfairis/issues/83)
- adhere to fair-software recommendations [#50](https://github.com/fair-software/howfairis/issues/50) [#53](https://github.com/fair-software/howfairis/issues/53) [#137](https://github.com/fair-software/howfairis/issues/137) [#151](https://github.com/fair-software/howfairis/pull/151)
- support for more anaconda badges [#124](https://github.com/fair-software/howfairis/issues/124)
- warning for commented badges in README.rst [#72](https://github.com/fair-software/howfairis/issues/72)
- quiet mode to the cli [#182](https://github.com/fair-software/howfairis/issues/182)
- Readme.get_compliance() [#94](https://github.com/fair-software/howfairis/issues/94)
- retrieve the default branch [#48](https://github.com/fair-software/howfairis/issues/48)

### Changed
- automated tests for Python 3.6, 3.7, 3.8, 3.9 [#80](https://github.com/fair-software/howfairis/issues/80)
- rename configuration keys [#164](https://github.com/fair-software/howfairis/issues/164) [#179](https://github.com/fair-software/howfairis/issues/179)
- users can now add a reason if they want to skip a check [#179](https://github.com/fair-software/howfairis/issues/179)
- Config class is merged into the Checker class [#172](https://github.com/fair-software/howfairis/issues/172) [#194](https://github.com/fair-software/howfairis/issues/194)
- Checker.check_five_recommendations() now returns Compliance object [#145](https://github.com/fair-software/howfairis/issues/145)
- moved badge generation to Compliance class [#94](https://github.com/fair-software/howfairis/issues/94)
- renamed config related argument names of cli [#172](https://github.com/fair-software/howfairis/issues/172) [#194](https://github.com/fair-software/howfairis/issues/194)

### Removed
- option to set compliant symbol [#178](https://github.com/fair-software/howfairis/issues/178)
- config argument from the Repo constructor [#194](https://github.com/fair-software/howfairis/issues/194)

## [0.12.0] - 2020-December-09

We started to keep a changelog after this release.

[Unreleased]: https://github.com/fair-software/howfairis/compare/0.14.2..HEAD
[0.14.2]: https://github.com/fair-software/howfairis/compare/0.14.1..0.14.2
[0.14.1]: https://github.com/fair-software/howfairis/compare/0.14.0..0.14.1
[0.14.0]: https://github.com/fair-software/howfairis/compare/0.13.0..0.14.0
[0.13.0]: https://github.com/fair-software/howfairis/compare/0.12.0..0.13.0
[0.12.0]: https://github.com/fair-software/howfairis/releases/tag/0.12.0
