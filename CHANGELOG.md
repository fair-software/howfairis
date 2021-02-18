# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


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


[Unreleased]: https://github.com/fair-software/howfairis/compare/0.13.0...HEAD
[0.13.0]: https://github.com/fair-software/howfairis/compare/0.12.0...0.13.0
[0.12.0]: https://github.com/fair-software/howfairis/releases/tag/0.12.0
