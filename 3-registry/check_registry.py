import os

def has_pypi_badge(readme_file):
    with open(readme_file) as text:
        for line in text:
            if 'PyPi' in line or 'pypi' in line:
                return "PyPi is found"

    return "No registry found"


def main():
    print(has_pypi_badge("README.md"))


if __name__ == "__main__":
    main()
