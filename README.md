# howfairis

Python package to analyze a GitHub repository's compliance with the fair-software.eu recommendations.


Install

```
# while the package has not been released on PyPI yet, install with
pip3 install --user git+https://github.com/fair-software/howfairis

# Use it like this
howfairis https://github.com/owner/repo
```

Development install

```shell
# Create a virtualenv, e.g. with
python3 -m virtualenv -p python3 venv3

# activate virtualenv
source venv3/bin/activate

# (from the project root directory)
# install howfairis as an editable package
pip install --editable .
pip install --editable .[dev]

# You should now have a command line utility 
# 'howfairis' (whenever you are in the virtualenv):
howfairis https://github.com/owner/repo

```


# For maintainers


Bumping the version across all files is done with bump2version, e.g.

```shell
bump2version --current-version 0.1.0 major|minor|patch
```
