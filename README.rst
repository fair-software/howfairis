``howfairis``
=============

Python package to analyze a GitHub repository's compliance with the
fair-software.eu recommendations.

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

Afterwards check that the install directory was added to the ``PATH``
environment variable. You should then be able to call the executable,
like so:

.. code:: shell

    howfairis https://github.com/owner/repo      # Linux | Mac
    howfairis.exe https://github.com/owner/repo  # Windows

Expected output
---------------

Depending on for which repository you are doing the analysis, the output
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
          × has_sonarcloud_badge

    Calculated compliance: ● ● ● ● ●

    Expected badge is equal to the actual badge. It's all good.
    
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
