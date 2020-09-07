# howfairis

Python package to analyze a GitHub repository's compliance with the fair-software.eu recommendations.


## Install

```shell
# while the package has not been released on PyPI yet, install with
pip3 install --user git+https://github.com/fair-software/howfairis
```

Afterwards check that the install directory was added to the 
``PATH`` environment variable. You should then be able to call the 
executable, like so:

```shell
howfairis https://github.com/owner/repo      # Linux | Mac
howfairis.exe https://github.com/owner/repo  # Windows
```

## Development install

```shell
# Create a virtualenv, e.g. with
python3 -m virtualenv -p python3 venv3

# activate virtualenv
source venv3/bin/activate

# (from the project root directory)
# install howfairis as an editable package
pip install --editable .
pip install --editable .[dev]
```

Afterwards check that the install directory was added to the 
``PATH`` environment variable. You should then be able to call the 
executable, like so:

```shell
howfairis https://github.com/owner/repo      # Linux | Mac
howfairis.exe https://github.com/owner/repo  # Windows
```


## For maintainers


Bumping the version across all files is done with bump2version, e.g.

```shell
bump2version minor
```
