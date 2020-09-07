``howfairis``
=============

Python package to analyze a GitHub repository's compliance with the
fair-software.eu recommendations.

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
            has_open_repository: true
    (2/5) license
            has_license: true
    (3/5) registry
            has_pypi_badge: true
            has_conda_badge: false
            has_bintray_badge: false
            is_on_github_marketplace: false
    (4/5) citation
            has_zenodo_badge: true
            has_citationcff_file: false
            has_citation_file: false
            has_zenodo_metadata_file: false
            has_codemeta_file: false
    (5/5) checklist
            has_core_infrastructures_badge: true
            has_sonarcloud_badge: false

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

    cd $(mktemp -d)
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

    # install in user space from test pypi instance:
    python3 -m pip -v install --user --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple howfairis

    # check that the package works as it should when installed from pypitest

    # FINAL STEP: upload to PyPI
    twine upload dist/*
