## Checklist

- [ ] Code follows the [contributing guidelines](CONTRIBUTING.rst) of the project
- [ ] This PR solves an existing issue and provided solution was discussed
- [ ] The fix has been locally tested
- [ ] Code follows the project's coding standards
- [ ] Unit tests covering the new feature have been added
- [ ] All existing tests pass
- [ ] The documentation has been updated to reflect the new feature

## List of related issues or pull requests

- #ISSUE_NUMBER
- #ISSUE_NUMBER

## Briefly describe the changes made in this pull request


## Additional Notes

Any additional information or context relevant to this PR.


## Instructions to review the pull request

```shell
# make a new temporary directory and cd into it
cd $(mktemp -d --tmpdir howfairis.XXXXXX)

# get a copy of the repo
git clone https://github.com/fair-software/howfairis .

# checkout the work from this branch 
git checkout <this branch>

# create a virtual environment named venv3
python3 -m venv venv3

# activate the virtual environment
source venv3/bin/activate

# update pip and friends
python3 -m pip install --upgrade pip wheel setuptools

# install runtime dependencies
python3 -m pip install .

# and, if you need it, the development tools
python3 -m pip install .[dev]
```

Keep what you need from below, extend as necessary

```shell
# run the unit tests
pytest

# tests against a live infrastructure
pytest livetests/

# cli tests
bash clitests/script.sh

# run linter
prospector

# import style
isort --check-only howfairis

# any additional steps for checking
```

