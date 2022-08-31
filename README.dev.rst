``howfairis`` developer documentation
=====================================

If you're looking for user documentation, go `here <README.rst>`_.

|
|

Development install
-------------------

.. code:: shell

    # Create a virtualenv, e.g. with
    python3 -m venv venv3

    # activate virtualenv
    source venv3/bin/activate
    
    # make sure to have a recent version of pip, wheel, setuptools
    python3 -m pip install --upgrade pip wheel setuptools

    # (from the project root directory)
    # install howfairis as an editable package, with development dependencies
    python3 -m pip install --no-cache-dir --editable .[dev]

Afterwards check that the install directory is present on the ``PATH``
environment variable. If so, you should  be able to call the executable,
like so:

.. code:: shell

    howfairis https://github.com/<owner>/<repo>

Running the tests
-----------------

Running the tests requires an activated virtualenv with the development tools installed.

.. code:: shell

    # unit tests with mocked representations of repository behavior
    pytest
    pytest tests/
    
    # live tests with actual repository behavior (slow, prone to HttpError too many requests)
    pytest livetests/
    
    # command line interface tests
    bash clitests/script.sh

Running linters locally
-----------------------

Running the linters requires an activated virtualenv with the development tools installed.

.. code:: shell

    # linter
    prospector

    # recursively check import style for the howfairis module only
    isort --check-only howfairis

    # recursively check import style for the howfairis module only and show
    # any proposed changes as a diff
    isort --check-only --diff howfairis

    # recursively fix  import style for the howfairis module only
    isort howfairis

.. code:: shell

    # requires activated virtualenv with development tools
    prospector && isort --check-only howfairis

You can enable automatic linting with ``prospector`` and ``isort`` on commit like so:

.. code:: shell

    git config --local core.hooksPath .githooks

Versioning
----------

Bumping the version across all files is done with bump2version, e.g.

.. code:: shell

    bump2version minor


Making a release
----------------

Preparation
^^^^^^^^^^^

1. Update the ``CHANGELOG.md``
2. Verify that the information in ``CITATION.cff`` is correct
3. Make sure the version has been updated.
4. Run the unit tests with ``pytest tests/``
5. Run the live tests with ``pytest livetests/``
6. Run the clitests with ``bash clitests/script.sh``

PyPI
^^^^

In a new terminal, without an activated virtual environment or a venv3 directory:

.. code:: shell

    # prepare a new directory
    cd $(mktemp -d --tmpdir howfairis.XXXXXX)
    
    # fresh git clone ensures the release has the state of origin/main branch
    git clone https://github.com/fair-software/howfairis.git .
    
    # prepare a clean virtual environment and activate it
    python3 -m venv venv3
    source venv3/bin/activate
    
    # make sure to have a recent version of pip, wheel, setuptools
    python3 -m pip install --upgrade pip wheel setuptools

    # install runtime dependencies and publishing dependencies
    python3 -m pip install --no-cache-dir .[publishing]
    
    # clean up any previously generated artefacts 
    rm -rf howfairis.egg-info
    rm -rf dist
    
    # create the source distribution and the wheel
    python3 setup.py sdist bdist_wheel

    # upload to test pypi instance (requires credentials)
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

In a new terminal, without an activated virtual environment or a venv3 directory:

.. code:: shell
    
    cd $(mktemp -d --tmpdir howfairis-test.XXXXXX)

    # check you don't have an existing howfairis
    which howfairis
    python3 -m pip uninstall howfairis

    # install in user space from test pypi instance:
    python3 -m pip -v install --user --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple howfairis

Check that the package works as it should when installed from pypitest.

Then upload to pypi.org with:

.. code:: shell

    # Back to the first terminal,
    # FINAL STEP: upload to PyPI (requires credentials)
    twine upload dist/*

GitHub and Zenodo
^^^^^^

1. Make a release on GitHub
2. Verify that making the GitHub release triggered Zenodo into making an archived snapshot of the release.

DockerHub
^^^^^^^^^

To build the image, run:

.. code:: shell

    docker build -t fairsoftware/howfairis:latest .
    
.. code:: shell

    VERSION=$(howfairis --version | sed 's/version: //g')
    docker tag fairsoftware/howfairis:latest fairsoftware/howfairis:${VERSION}

Check that you have the tags you want with:

.. code:: shell

    docker images

To push the image to DockerHub, run:

.. code:: shell

    # (requires credentials)  
    docker login
    docker push fairsoftware/howfairis:${VERSION}
    docker push fairsoftware/howfairis:latest    
    
The new image and its tags should now be listed here https://hub.docker.com/r/fairsoftware/howfairis/tags?page=1&ordering=last_updated.
    
