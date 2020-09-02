def has_pypi_badge(readme_file):
    with open(readme_file) as text:
        for line in text:
            if 'PyPi' in line or 'pypi' in line:
                return "PyPi is found"

    return "No PyPi"


def main():
    print(has_pypi_badge("some test string with the workd PyPI in it"))


if __name__ == "__main__":
    main()
