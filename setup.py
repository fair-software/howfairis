import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open("README.rst", "rt", encoding="UTF-8") as readme_file:
    readme = readme_file.read()

setup(
    name="howfairis",
    entry_points={
        "console_scripts": ["howfairis=howfairis.cli.cli:cli"],
    },
    version="0.15.0",
    description="Python package to analyze compliance with fair-software.eu recommendations",
    long_description=readme + "\n\n",
    author="The Netherlands eScience Center",
    author_email="info@esciencecenter.nl",
    url="https://github.com/fair-software/howfairis",
    packages=[
        "howfairis",
        "howfairis.cli",
        "howfairis.exceptions",
        "howfairis.mixins",
        "howfairis.requesting",
        "howfairis.workarounds",
    ],
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="howfairis",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    test_suite="tests",
    install_requires=[
        "backoff==2.2.*",
        "beautifulsoup4==4.12.*",
        "click==8.1.*",
        "colorama==0.4.*",
        "docutils==0.21.*",
        "Pygments==2.18.*",
        "ratelimit==2.2.*",
        "requests==2.32.*",
        "ruamel.yaml==0.18.*",
        "voluptuous==0.15.*",
    ],
    setup_requires=[],
    tests_require=[],
    extras_require={
        "dev": [
            "bumpversion",
            "prospector[with_pyroma]",
            "pycodestyle",
            "pytest-cov",
            "pytest-runner",
            "pytest",
            "recommonmark",
            "requests_mock",
            "sphinx_rtd_theme",
            "sphinx-click",
            "sphinx",
            "yapf",
        ],
        "publishing": ["twine", "wheel"],
    },
    data_files=[],
)
