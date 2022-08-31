**List of related issues or pull requests**

Refs: #ISSUE_NUMBER

**Describe the changes made in this pull request**

**Instructions to review the pull request**

```shell
# make a new temporary directory and cd into it
cd $(mktemp -d --tmpdir howfairis.XXXXXX)

# get a copy of the repo
git clone https://github.com/fair-software/howfairis .

# checkout the work from this branch 
git checkout <this branch>

# update pip and friends
python3 -m pip install --upgrade pip wheel setuptools

# install runtime dependencies
python3 -m pip install .

# and, if you need it, the development tools
python3 -m pip install .[dev]

<write additional steps for checking here>
```

