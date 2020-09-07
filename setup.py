import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open("README.rst", "rt", encoding="UTF-8") as readme_file:
    readme = readme_file.read()

setup(
    name="howfairis",
    entry_points={
        "console_scripts": ["howfairis=howfairis.cli:cli"],
    },
    version="0.4.1",
    description="Python package to analyze compliance with fair-software.eu recommendations",
    long_description=readme + "\n\n",
    author="https://github.com/jspaaks",
    author_email="j.spaaks@esciencecenter.nl",
    url="https://github.com/fair-software/howfairis",
    packages=["howfairis", "howfairis.mixins"],
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="howfairis",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    install_requires=[
        "requests",
        "colorama"
    ],
    setup_requires=[
    ],
    tests_require=[
    ],
    extras_require={
        "dev":  [
            "prospector[with_pyroma]",
            "yapf",
            "bumpversion",
            "pytest",
            "pytest-cov",
            "pycodestyle",
            "pytest-runner"
        ],
        "publishing": [
            "twine"
        ]
    },
    data_files=[]
)
