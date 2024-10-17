howfairis
=========

|

Python package to analyze a GitHub or GitLab repository's compliance with the
fair-software.eu_ recommendations.

Badges
------


====================================================== ============================
fair-software.nl recommendations
====================================================== ============================
(1/5) code repository                                  |github repo badge|
(2/5) license                                          |github license badge|
(3/5) community registry                               |pypi badge|
(4/5) citation                                         |zenodo badge|
(5/5) checklist                                        |core infrastructures badge|
overall                                                |fair-software badge|
**Other best practices**
Documentation                                          |readthedocs badge|
Supported Python versions                              |python versions badge| 
Code quality                                           |sonarcloud quality badge|
Code coverage of unit tests                            |sonarcloud coverage badge|
DockerHub                                              |dockerhub badge|
**GitHub Actions**
cffconvert                                             |workflow cffconvert badge|
Unit tests                                             |workflow tests badge|
Live tests (triggered manually)                        |workflow livetests badge|
====================================================== ============================

.. |github repo badge| image:: https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue
   :target: https://github.com/fair-software/howfairis

.. |github license badge| image:: https://img.shields.io/github/license/fair-software/howfairis
   :target: https://github.com/fair-software/howfairis

.. |pypi badge| image:: https://img.shields.io/pypi/v/howfairis.svg?colorB=blue
   :target: https://pypi.python.org/pypi/howfairis/

.. |zenodo badge| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4017908.svg
   :target: https://doi.org/10.5281/zenodo.4017908
   
.. |core infrastructures badge| image:: https://bestpractices.coreinfrastructure.org/projects/4630/badge
   :target: https://bestpractices.coreinfrastructure.org/en/projects/4630

.. |fair-software badge| image:: https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green
   :target: https://fair-software.eu
   
.. |readthedocs badge| image:: https://readthedocs.org/projects/howfairis/badge/?version=latest
   :target: https://howfairis.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
   
.. |python versions badge| image:: https://img.shields.io/pypi/pyversions/howfairis.svg
   :target: https://pypi.python.org/pypi/howfairis   

.. |sonarcloud quality badge| image:: https://sonarcloud.io/api/project_badges/measure?project=fair-software_howfairis&metric=alert_status
   :target: https://sonarcloud.io/dashboard?id=fair-software_howfairis
   :alt: Quality Gate Status

.. |sonarcloud coverage badge| image:: https://sonarcloud.io/api/project_badges/measure?project=fair-software_howfairis&metric=coverage
   :target: https://sonarcloud.io/dashboard?id=fair-software_howfairis
   :alt: Coverage

.. |dockerhub badge| image:: https://img.shields.io/docker/pulls/fairsoftware/howfairis
   :target: https://hub.docker.com/r/fairsoftware/howfairis
   :alt: Docker Pulls

.. |workflow tests badge| image:: https://github.com/fair-software/howfairis/workflows/tests/badge.svg
   :target: https://github.com/fair-software/howfairis/actions?query=workflow%3Atests

.. |workflow livetests badge| image:: https://github.com/fair-software/howfairis/workflows/livetests/badge.svg
   :target: https://github.com/fair-software/howfairis/actions?query=workflow%3Alivetests

.. |workflow cffconvert badge| image:: https://github.com/fair-software/howfairis/workflows/cffconvert/badge.svg
   :target: https://github.com/fair-software/howfairis/actions?query=workflow%3A%22cffconvert%22

Install
-------

.. code:: console

    pip3 install --user howfairis

Verify that the install directory is on the ``PATH`` environment variable. If so,
you should be able to call the executable, like so:

.. code:: console

    howfairis https://github.com/<owner>/<repo>


``howfairis`` supports URLs from the following code repository platforms:

1. ``https://github.com``
2. ``https://gitlab.com`` (not including self-hosted instances)

Docker
---------------

You can run howfairis Docker image using the command below.

.. code:: console

    docker pull fairsoftware/howfairis

You can run howfairis Docker image using the command below.

.. code:: console

    docker run --rm fairsoftware/howfairis --help

`--rm` argument will remove Docker container after execution.

See developer documentation to learn how to modify the Docker image.

Expected output
---------------

Depending on which repository you are doing the analysis for, the output
looks something like this:

.. code:: console

    Checking compliance with fair-software.eu...
    url: https://github.com/fair-software/badge-test
    (1/5) repository
          ✓ has_open_repository
    (2/5) license
          ✓ has_license
    (3/5) registry
          × has_ascl_badge
          × has_bintray_badge
          × has_conan_badge
          × has_conda_badge
          × has_cran_badge
          × has_crates_badge
          × has_maven_badge
          × has_npm_badge
          ✓ has_pypi_badge
          × has_rsd_badge
          × is_on_github_marketplace
    (4/5) citation
          × has_citation_file
          × has_citationcff_file
          × has_codemeta_file
          ✓ has_zenodo_badge
          × has_zenodo_metadata_file
    (5/5) checklist
          ✓ has_core_infrastructures_badge

If your README already has the fair-software badge, you'll see some output like this:

.. code:: console

    Calculated compliance: ● ● ○ ● ●

    Expected badge is equal to the actual badge. It's all good.

If your README doesn't have the fair-software badge yet, or its compliance is different from what's been calculated,
you'll see output like this:

.. code:: console

    Calculated compliance: ● ● ○ ○ ○

    It seems you have not yet added the fair-software.eu badge to
    your README.md. You can do so by pasting the following snippet:

    [![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8B-orange)](https://fair-software.eu)

When you get this message, just copy-and-paste the suggested badge into your README.

Some examples of badges
-----------------------

The color of the badge depends on the level of compliance; the pattern of filled and empty circles will vary depending
on which recommendations the repository complies with.

Each circle represents one of the recommendations, meaning the first symbol represents the first recommendation, *Use a
publicly accessible repository with version control*, the second symbol represents the second recommendation, and so on.
You can find more information about the recommendations on fair-software.eu_.

.. image:: https://img.shields.io/badge/fair--software.eu-%E2%97%8B%20%20%E2%97%8B%20%20%E2%97%8F%20%20%E2%97%8B%20%20%E2%97%8B-red

The state of the third circle indicates the software has been registered in a community registry. Since the repository
only complies with one of the recommendations, this badge gets a red color.

.. image:: https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8B%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-orange

The repository with this badge complies with 3 out of 5 recommendations, hence its color is orange. From the open/closed
state of the circles, it is a publicly accessible repository with version control. It has been registered in a community
registry, and it contains citation information. There is no license in this repository, and the project does not use a
checklist.

.. image:: https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow

Almost complete compliance yields a yellow badge. The corresponding repository meets all the recommendations except
the one that calls for adding a checklist.

.. image:: https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green

Perfect compliance!

More options
------------

There are some command line options to the executable. You can see them using:

.. code:: console

    howfairis --help

Which then shows something like:

.. code:: console

    Usage: howfairis [OPTIONS] [URL]

      Determine compliance with recommendations from fair-software.eu for the
      repository at URL. The following code repository platforms are supported:

      * https://github.com

      * https://gitlab.com (not including any self-hosted instances)

    Options:
      -b, --branch TEXT               Which git branch to use. Also accepts other
                                      git references like SHA or tag.

      -u, --user-config-filename PATH
                                      Name of the configuration file to control
                                      howfairis'es behavior. The configuration
                                      file needs to be present on the local system
                                      and can include a relative path.

      -d, --show-default-config       Show default configuration and exit.
      -i, --ignore-repo-config        Ignore any configuration files on the
                                      remote.

      -p, --path TEXT                 Relative path (on the remote). Use this if
                                      you want howfairis to look for a README and
                                      a configuration file in a subdirectory.

      -q, --quiet                     Use this flag to disable all printing except
                                      errors.

      -r, --repo-config-filename TEXT
                                      Name of the configuration file to control
                                      howfairis'es behavior. The configuration
                                      file needs to be on the remote, and takes
                                      into account the value of --branch and
                                      --path. Default: .howfairis.yml

      -t, --show-trace                Show full traceback on errors.
      -v, --version                   Show version and exit.
      -h, --help                      Show this message and exit.

Configuration file
^^^^^^^^^^^^^^^^^^

Each category of checks can be skipped using a configuration file. This file needs to be present at ``URL``, taking into
account the values passed with ``--path`` and with ``--repo-config-filename``.

The configuration file should follow the voluptuous_ schema laid out in schema.py_:

.. code:: python

    schema = {
        Optional("skip_repository_checks_reason"): Any(str, None),
        Optional("skip_license_checks_reason"): Any(str, None),
        Optional("skip_registry_checks_reason"): Any(str, None),
        Optional("skip_citation_checks_reason"): Any(str, None),
        Optional("skip_checklist_checks_reason"): Any(str, None),
        Optional("ignore_commented_badges"): Any(bool, None)
    }

For example, the following is a valid configuration file document:

.. code:: yaml

    ## Uncomment a line if you want to skip a given category of checks

    #skip_repository_checks_reason: <reason for skipping goes here>
    #skip_license_checks_reason: <reason for skipping goes here>
    #skip_registry_checks_reason: <reason for skipping goes here>
    #skip_citation_checks_reason: <reason for skipping goes here>
    skip_checklist_checks_reason: "I'm using the Codacy dashboard to guide my development"

    ignore_commented_badges: false


The manual override will be reflected in the output, as follows:

.. code:: console

    (1/5) repository
          ✓ has_open_repository
    (2/5) license
          ✓ has_license
    (3/5) registry
          × has_ascl_badge
          × has_bintray_badge
          × has_conan_badge
          × has_conda_badge
          × has_cran_badge
          × has_crates_badge
          × has_maven_badge
          × has_npm_badge
          ✓ has_pypi_badge
          × has_rsd_badge
          × is_on_github_marketplace
    (4/5) citation
          × has_citation_file
          ✓ has_citationcff_file
          × has_codemeta_file
          ✓ has_zenodo_badge
          ✓ has_zenodo_metadata_file
    (5/5) checklist
          ✓ skipped (reason: I'm using the Codacy dashboard to guide my development)

Rate limit
^^^^^^^^^^

By default ``howfairis`` uses anonymous requests to the API of the source code platforms.
However when a lot of repositories are checked you will exceed the rate limit of those APIs and checks will fail.
To increase the rate limit you need to use authenticated requests.
Your username and token can be passed to ``howfairis`` using environment variables called ``APIKEY_GITHUB`` and ``APIKEY_GITLAB``.
The format of the environment variable values are:

.. code-block:: shell

  export APIKEY_GITHUB=<user who made the token>:<personal access token>
  export APIKEY_GITLAB=<user who made the token>:<personal access token>

Generation of personal access tokens are explained on `GitHub documentation <https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token>`_ and `GitLab documentation <https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#creating-a-personal-access-token>`_.
No scopes have to be selected, being authenticated is enough to get higher rate limit.

Contributing
------------

If you want to contribute to the development of howfairis, have a look at the `contribution guidelines <CONTRIBUTING.rst>`_.

If you're looking for developer documentation, go `here <README.dev.rst>`_.

.. _fair-software.eu: https://fair-software.eu
.. _voluptuous: https://pypi.org/project/voluptuous/
.. _schema.py: https://github.com/fair-software/howfairis/blob/master/howfairis/schema.py

Credits
-------

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ and the `NLeSC/python-template <https://github.com/NLeSC/python-template>`_.
