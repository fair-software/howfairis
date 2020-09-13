``howfairis``
=============

Python package to analyze a GitHub or GitLab repository's compliance with the
fair-software.eu_ recommendations.

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4017908.svg
   :target: https://doi.org/10.5281/zenodo.4017908
   
.. image:: https://img.shields.io/pypi/v/howfairis.svg?colorB=blue 
   :target: https://pypi.python.org/pypi/howfairis/
   
.. image:: https://github.com/fair-software/howfairis/workflows/Build/badge.svg
   :target: https://github.com/fair-software/howfairis/actions?query=workflow%3ABuild

.. image:: https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow
   :target: https://fair-software.eu

Install
-------

.. code:: shell

    pip3 install --user howfairis

Verify that the install directory is on the ``PATH`` environment variable. If so,
you should be able to call the executable, like so:

.. code:: shell

    howfairis https://github.com/owner/repo      # Linux | Mac
    howfairis.exe https://github.com/owner/repo  # Windows

Expected output
---------------

Depending on which repository you are doing the analysis for, the output
looks something like this:

.. code:: shell

    Checking compliance with fair-software.eu...
    Running for https://github.com/fair-software/badge-test
    (1/5) repository
          ✓ has_open_repository
    (2/5) license
          ✓ has_license
    (3/5) registry
          × has_bintray_badge
          × has_conda_badge
          × has_cran_badge
          × has_crates_badge
          × has_maven_badge
          × has_npm_badge
          × has_pypi_badge
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
          × has_sonarcloud_badge

If your README already has the fair-software badge, you'll see some output like this:

.. code:: shell

    Calculated compliance: ● ● ○ ● ●

    Expected badge is equal to the actual badge. It's all good.
    
If your README doesn't have the fair-software badge yet, or its compliance is different from what's been calculated,
you'll see output like this:

.. code:: shell

    Calculated compliance: ● ● ○ ○ ○

    While searching through your README.md, I did not find the expected badge:
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

.. code:: shell

    howfairis --help

Which then shows something like:

.. code:: shell

    Usage: howfairis [OPTIONS] [URL]...

      Determine compliance with recommendations from fair-software.eu for the
      GitHub or GitLab repository at URL.

    Options:
      -b, --branch TEXT       Which git branch to use.
      -c, --config-file PATH  Config file. Default: .howfairis.yml
      -p, --path TEXT         Relative path.
      -s, --show-trace        Show full traceback on errors. Default: False
      -v, --version           Show version
      --help                  Show this message and exit.

Configuration file
^^^^^^^^^^^^^^^^^^

The state of each check can be forced using a configuration file. This file needs to be present at ``URL``, taking into
account the values passed with ``--path`` and with ``--config-file``.

The configuration file should follow the voluptuous_ schema laid out in schema.py_:

.. code:: python

    {
        Optional("force"): {
            Optional("repository"): bool,
            Optional("license"): bool,
            Optional("registry"): bool,
            Optional("citation"): bool,
            Optional("checklist"): bool,
        }
    }

For example, the following is a valid configuration file document:

.. code:: yaml

    force:
      registry: true  # It is good practice to add an explanation
                      # of why you chose to set the state manually

The manual override will be reflected in the output, as follows:

.. code:: shell

    (1/5) repository
          ✓ has_open_repository
    (2/5) license
          ✓ has_license
    (3/5) registry: force True
    (4/5) citation
          × has_citation_file
          × has_citationcff_file
          × has_codemeta_file
          × has_zenodo_badge
          × has_zenodo_metadata_file
    (5/5) checklist
          × has_core_infrastructures_badge
          × has_sonarcloud_badge

Development install
-------------------

.. code:: shell

    # Create a virtualenv, e.g. with
    python3 -m virtualenv -p python3 venv3

    # activate virtualenv
    source venv3/bin/activate

    # (from the project root directory)
    # install howfairis as an editable package
    pip install --editable .
    pip install --editable .[dev]

Afterwards check that the install directory was added to the ``PATH``
environment variable. You should then be able to call the executable,
like so:

.. code:: shell

    howfairis https://github.com/owner/repo      # Linux | Mac
    howfairis.exe https://github.com/owner/repo  # Windows

For maintainers
---------------

Bumping the version across all files is done with bump2version, e.g.

.. code:: shell

    bump2version minor


Making a release
^^^^^^^^^^^^^^^^

Make sure the version is correct.

.. code:: shell
    
    # In a new terminal, without venv
    cd $(mktemp -d --tmpdir howfairis.XXXXXX)
    git clone https://github.com/fair-software/howfairis.git .
    python3 -m virtualenv -p python3 venv3
    source venv3/bin/activate
    pip install --no-cache-dir --editable .
    pip install --no-cache-dir --editable .[publishing]
    rm -rf howfairis.egg-info
    rm -rf dist
    python setup.py sdist

    # upload to test pypi instance
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    # In a new terminal, without venv
    
    # check you don't have an existing howfairis
    python3 -m pip uninstall howfairis

    # install in user space from test pypi instance:
    python3 -m pip -v install --user --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple howfairis

    # check that the package works as it should when installed from pypitest

    # Back to the first terminal,
    # FINAL STEP: upload to PyPI
    twine upload dist/*

Don't forget to also make a release on GitHub.


.. _fair-software.eu: https://fair-software.eu
.. _voluptuous: https://pypi.org/project/voluptuous/
.. _schema.py: https://github.com/fair-software/howfairis/blob/master/howfairis/schema.py
