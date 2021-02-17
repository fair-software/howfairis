``howfairis`` developer documentation
=====================================

If you're looking for user documentation, go `here <README.rst>`_.

|
|
|

Development install
-------------------

.. code:: shell

    # Create a virtualenv, e.g. with
    python3 -m venv venv3

    # activate virtualenv
    source venv3/bin/activate

    # (from the project root directory)
    # install howfairis as an editable package
    pip install --no-cache-dir --editable .
    # install development dependencies
    pip install --no-cache-dir --editable .[dev]

Afterwards check that the install directory was added to the ``PATH``
environment variable. You should then be able to call the executable,
like so:

.. code:: shell

    howfairis https://github.com/<owner>/<repo>

Docker
------
To build the image, run:

.. code:: shell

   docker build -t fairsoftware/howfairis .

To push the image to DockerHub, run:

.. code:: shell

   docker push fairsoftware/howfairis


Running linters locally
-----------------------

Running the linters requires an activated virtualenv with the development tools installed.

.. code:: shell

    # linter
    prospector

    # recursively check import style for the howfairis module only
    isort --recursive --check-only howfairis

    # recursively check import style for the howfairis module only and show
    # any proposed changes as a diff
    isort --recursive --check-only --diff howfairis

    # recursively fix  import style for the howfairis module only
    isort --recursive howfairis

.. code:: shell

    # requires activated virtualenv with development tools
    prospector && isort --recursive --check-only howfairis

You can enable automatic linting with ``prospector`` and ``isort`` on commit like so:

.. code:: shell

    git config --local core.hooksPath .githooks

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
    python3 -m venv venv3
    source venv3/bin/activate
    pip install --no-cache-dir .
    pip install --no-cache-dir .[publishing]
    rm -rf howfairis.egg-info
    rm -rf dist
    python setup.py sdist bdist_wheel

    # upload to test pypi instance
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    # In a new terminal, without an activated venv or a venv3 directory
    cd $(mktemp -d --tmpdir howfairis-test.XXXXXX)

    # check you don't have an existing howfairis
    which howfairis
    python3 -m pip uninstall howfairis

    # install in user space from test pypi instance:
    python3 -m pip -v install --user --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple howfairis

    # check that the package works as it should when installed from pypitest


Don't forget to also make a release on GitHub.

.. code:: shell

    # Back to the first terminal,
    # FINAL STEP: upload to PyPI
    twine upload dist/*


Credits
-------

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ and the `NLeSC/python-template <https://github.com/NLeSC/python-template>`_.
