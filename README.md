# howfairis

_GitHub action to assess compliance with fair-software.eu_

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
        with:
          MY_REPO_URL: "https://github/com/${{ github.repository }}"
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

# badge

This badge describes and visualises the compliance with FAIR Sofatware
recommendations as described on [fair-software.eu website](https://fair-software.eu/) site.
The [Netherlands eScience Center](https://www.esciencecenter.nl/) and [DANS](https://dans.knaw.nl/) launched fair-software.eu with five
actionable and practical recommendations that help researchers to make their
software more FAIR (Findable, Accessible, Interoperable, Reusable).

Read more about how to interpret the badge in the [fair-badge-explained](fair-badge-explained.md) document.

## What do we mean by compliance
The badge action does checks on the repository it runs on.

### [Repository](https://fair-software.eu/recommendations/repository)
Is this software in a version controlled repository (eg. GitHub or Gitlab)?
Is this repository open?

### [License](https://fair-software.eu/recommendations/license)
Is there a license file? The license does not have to be OSI approved license, but it has to be one of the standard licenses.

### [Registry](https://fair-software.eu/recommendations/registry)
Is this software registered in one or more software registry. You can find an extensive list of registries in the [Awesome Research Software Registries](https://github.com/NLeSC/awesome-research-software-registries)

### [Citation](https://fair-software.eu/recommendations/citation)
Does the repository contain the description on how to cite the software? This can be done in the form of CITATION.cff file, that uses [Citation File Format](https://citation-file-format.github.io/), or plain CITATION file.

### [Checklist](https://fair-software.eu/recommendations/checklist)
Do the developers of the software use a software quiality checklist?
