# howfairis

Python package to analyze a GitHub repository's compliance with the fair-software.eu recommendations.


Install

```
# while the package has not been released on PyPI yet, install with
pip install --user git+https://github.com/fair-software/howfairis
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

# You should now have a command line utility 
# 'howfairis' (whenever you are in the virtualenv):
howfairis https://github.com/owner/repo

```
