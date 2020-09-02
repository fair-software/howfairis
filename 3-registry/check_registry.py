def has_pypi_badge(readme_string):
    return readme_string.lower().find("pypi") != -1


def main():
    has_pypi_badge("some test string with the workd PyPI in it")


if __name__ == "__main__":
    main()
