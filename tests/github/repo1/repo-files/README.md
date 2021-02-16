(mocked content)

# Assess compliance with fair-software.eu

To enable this checker, add the following snippet as ``.github/workflows/fair-software.yml`` in your GitHub repository.

```yaml
name: fair-software

on: push

jobs:
  verify:
    name: "fair-software"
    runs-on: ubuntu-latest
    steps:
      - uses: fair-software/badge@master
        name: Measure compliance with fair-software.eu recommendations
        env:
          PYCHARM_HOSTED: "Trick colorama into displaying colored output" 
        with:
          MY_REPO_URL: "https://github.com/${{ github.repository }}"
```

## FAIR badges explained

This GitHub action will suggest a badge visualizing compliance with the FAIR Software
recommendations as described on [fair-software.eu](https://fair-software.eu/).

The [Netherlands eScience Center](https://www.esciencecenter.nl/) and [DANS](https://dans.knaw.nl/) launched
fair-software.eu with five actionable and practical recommendations that help researchers to make their software more
FAIR (Findable, Accessible, Interoperable, Reusable).

### What do we mean by compliance

The GitHub Action does checks on the repository it runs on, and rates the repository according to these 5 aspects:

1. [``repository``](https://fair-software.eu/recommendations/repository): Is the software in a publicly accessible
repository with version control?
1. [``license``](https://fair-software.eu/recommendations/license): Is there a license file? The license does not have
to be OSI approved license, but it has to be one of the standard licenses.
1. [``registry``](https://fair-software.eu/recommendations/registry): Is the software registered in one or more software
registries? You can find an extensive list of registries in the [Awesome Research Software
Registries](https://github.com/NLeSC/awesome-research-software-registries)
1. [``citation``](https://fair-software.eu/recommendations/citation): Can the repository be cited easily? For example,
this can be done by including a ``CITATION.cff`` file, that uses [Citation File
Format](https://citation-file-format.github.io/).
1. [``checklist``](https://fair-software.eu/recommendations/checklist): Do the developers of the software use a software
quality checklist?

Through this GitHub action and the badges that it generates, we want to incentivize Research Software Engineers and
researchers who develop software to implement these Five recommendations for FAIR software, by making their effort and
compliance with the [fair-software.eu](https://fair-software.eu) recommendations more visible to the rest of the world.
We also want to promote the recommendations to a wider audience.

### How to interpret FAIR badges?

The color of the badge depends on the level of compliance; the pattern of filled and empty circles will vary depending
what aspects the software complies with.

Each circle represents one of the recommendations, meaning the first symbol represents the first recommendation, _Use a
publicly accessible repository with version control_, the second symbol represents the second recommendations, and so
on. You can find more information about the recommendations on [fair-software.eu](https://fair-software.eu/).

#### Here are some examples:

![](https://img.shields.io/badge/fair--software.eu-%E2%97%8B%20%E2%97%8B%20%E2%97%8F%20%E2%97%8B%20%E2%97%8B-red)

This badge's red color means that the repository complies with 0 or 1 recommendations. The state of the third circle
indicates the software has been registered in a community registry.

![](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%E2%97%8B%20%E2%97%8F%20%E2%97%8F%20%E2%97%8B-orange)

The repository with this badge complies with 3 out of 5 recommendations, hence its color is orange. It is a publicly
accessible repository with version control. It has been registered in a community registry, and it contains citation
information. There is no license in this repository, and the project does not use a checklist.

![](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%E2%97%8F%20%E2%97%8F%20%E2%97%8F%20%E2%97%8B-yellow)

A yellow badge means the repository complies with 4 recommendations.

![](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%E2%97%8F%20%E2%97%8F%20%E2%97%8F%20%E2%97%8F-green)

A green badge means the repository complies with all 5 recommendations.

## For developers

Building the docker image:

```shell
# (from project root directory)
docker build -t howfairis .
```

Running the dockerized ``howfairis`` locally:

```shell
# show howfairis'es help
docker run -ti howfairis --help
```

```shell
# start the analysis for a github repo
docker run -ti howfairis https://github.com/owner/repo

# start the analysis for a gitlab repo
docker run -ti howfairis https://gitlab.com/owner/repo
```

```shell
# show howfairis'es version
docker run -ti howfairis --version
```
