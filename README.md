# badge
A badge for showing compliance with fair-software.eu

To enable this checker, add the following snippet as ``.github/workflows/fair-software.yml`` in your GitHub repository.

```yaml
name: fair-software

on: push

jobs:
  verify:
    name: "fair-software"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        name: Check out a copy of your repository

      - uses: fair-software/badge@master
        name: Measure compliance with fair-software.eu recommendations
```


Building the docker image:

```shell
# (from project root directory)
docker build -t howfairis .
```

Running the dockerized howfair is locally:

```shell
# (from project root directory)
docker run -ti howfairis
```

Non-dockerized howfairis:

```shell
# Create a virtualenv, e.g. with
python3 -m virtualenv venv3

# activate virtualenv
source venv3/bin/activate

# (from the project root directory)
# install howfairis as an editable package
pip install --editable .

# You should now have a command line utility 
# 'howfairis' (whenever you are in the virtualenv):
howfairis

```

